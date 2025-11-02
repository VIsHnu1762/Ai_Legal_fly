# classifier.py
import re
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load fine-tuned model if available, else fall back to keyword-based
try:
    tokenizer = AutoTokenizer.from_pretrained("./contract_classifier")
    model = AutoModelForSequenceClassification.from_pretrained("./contract_classifier")
    use_ml_classifier = True
except:
    use_ml_classifier = False

# Contract categories
CONTRACT_TYPES = {
    0: "🏠 Lease / Rental Agreement",
    1: "👨‍💼 Employment Agreement",
    2: "📦 Vendor Contract",
    3: "🔒 NDA (Non-Disclosure Agreement)",
    4: "📄 General Contract"
}

def detect_contract_type(text: str) -> str:
    if use_ml_classifier:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        outputs = model(**inputs)
        pred = torch.argmax(outputs.logits, dim=1).item()
        return CONTRACT_TYPES.get(pred, "📄 General Contract")
    else:
        text_lower = text.lower()
        if "lease" in text_lower or "landlord" in text_lower or "tenant" in text_lower:
            return CONTRACT_TYPES[0]
        elif "employee" in text_lower or "employer" in text_lower or "salary" in text_lower:
            return CONTRACT_TYPES[1]
        elif "vendor" in text_lower or "purchase order" in text_lower:
            return CONTRACT_TYPES[2]
        elif "confidential" in text_lower or "non-disclosure" in text_lower:
            return CONTRACT_TYPES[3]
        else:
            return CONTRACT_TYPES[4]

def risk_score(contract_text):
    risky_keywords = {
        "penalty": ("High", "Could impose financial burden on the signer."),
        "termination": ("Medium", "The contract may be ended abruptly without enough notice."),
        "liability": ("High", "Exposes signer to potential unlimited responsibility."),
        "indemnify": ("High", "One party must cover losses/damages of the other."),
        "breach": ("Medium", "Strict consequences if obligations are not met."),
        "damages": ("Medium", "Compensation obligations in case of failure.")
    }

    score = 0
    findings = []

    for word, (severity, explanation) in risky_keywords.items():
        if word.lower() in contract_text.lower():
            weight = 3 if severity == "High" else 2
            score += weight
            findings.append({
                "term": word,
                "severity": severity,
                "explanation": explanation
            })

    return min(score, 10), findings