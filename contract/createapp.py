# createapp.py
import streamlit as st
import PyPDF2, pdfplumber, pytesseract
from pdf2image import convert_from_bytes
from transformers import pipeline
from classifier import detect_contract_type, risk_score
from deep_translator import GoogleTranslator

# -----------------------------
# 🔹 Helper Functions
# -----------------------------
def extract_text_with_ocr(file_bytes):
    """Extract text from scanned PDFs using OCR."""
    text = ""
    try:
        with pdfplumber.open(file_bytes) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        if not text.strip():  # OCR fallback
            images = convert_from_bytes(file_bytes.read())
            for img in images:
                text += pytesseract.image_to_string(img) + "\n"
    except Exception as e:
        st.error(f"❌ Error extracting text: {e}")
    return text


def translate_to_hindi(text: str) -> str:
    """Translate English text to Hindi."""
    try:
        return GoogleTranslator(source="en", target="hi").translate(text)
    except Exception as e:
        return f"⚠️ Translation failed: {e}"


def chunk_text(text, chunk_size=500):
    """Split text into smaller chunks for summarization."""
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i+chunk_size])


def detect_unfavorable_terms(text: str):
    """Identify unfavorable contract terms with explanations."""
    unfavorable_dict = {
        "termination without notice": "Allows one party to end the contract suddenly, leaving the other vulnerable.",
        "auto-renewal": "The contract may renew automatically without explicit consent, locking the business in.",
        "unlimited liability": "Exposes the SME to very high financial risk.",
        "non-compete": "Restricts the SME from doing other business activities, may be too broad.",
        "arbitration outside india": "Legal disputes may become costly and inconvenient if handled abroad."
    }

    findings = []
    text_lower = text.lower()

    for term, explanation in unfavorable_dict.items():
        if term in text_lower:
            idx = text_lower.find(term)
            snippet = text[max(0, idx - 50): idx + len(term) + 50]

            findings.append({
                "term": term,
                "explanation": explanation,
                "snippet": snippet.strip()
            })
    return findings


# -----------------------------
# 🔹 Streamlit App
# -----------------------------
st.set_page_config(page_title="Legal Contract Assistant", layout="wide")
st.title("⚖️ Legal Contract Assistant")
st.caption("A GenAI-powered assistant for contract analysis, risk detection, and legal insights.")

uploaded_file = st.file_uploader("📤 Upload a contract (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("📑 Extracting text..."):
        contract_text = ""
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    contract_text += page_text
        except Exception:
            contract_text = ""

        if not contract_text.strip():
            contract_text = extract_text_with_ocr(uploaded_file)

    # Tabs
    tabs = st.tabs([
        "📑 Contract Summary", 
        "⚠️ Risk Analysis", 
        "🌍 Language Support",
        "🚨 Unfavorable Terms"
    ])

    # -----------------------------
    # Tab 0: Contract Summary
    # -----------------------------
    with tabs[0]:
        st.subheader("📑 Contract Type")
        st.success(detect_contract_type(contract_text))

        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

        with st.spinner("📝 Summarizing..."):
            summary_chunks = []
            for chunk in chunk_text(contract_text):
                summary = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
                summary_chunks.append(summary[0]['summary_text'])
            final_summary = " ".join(summary_chunks)

        st.subheader("📝 Key Summary Points")
        for i, point in enumerate(final_summary.split(". ")):
            if point.strip():
                st.markdown(f"**{i+1}.** {point.strip()}")

        st.download_button("⬇️ Download Summary", final_summary, file_name="contract_summary.txt")

    # -----------------------------
    # Tab 1: Risk Analysis
    # -----------------------------
    with tabs[1]:
        st.subheader("⚠️ Risk Analysis")
        score, findings = risk_score(contract_text)

        st.metric("Overall Risk Score", f"{score}/10")

        if findings:
            for f in findings:
                severity_icon = "🔴" if f["severity"] == "High" else "🟠"
                with st.expander(f"{severity_icon} {f['term'].capitalize()} ({f['severity']} Risk)"):
                    st.write(f['explanation'])
        else:
            st.success("✅ No risky terms detected.")

    # -----------------------------
    # Tab 2: Language Support
    # -----------------------------
    with tabs[2]:
        st.subheader("🌍 Language Support")
        lang_choice = st.radio("Choose translation language:", ["English", "Hindi"], horizontal=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🇬🇧 English")
            st.info(final_summary)

        with col2:
            st.markdown("### 🇮🇳 Hindi")
            if lang_choice == "Hindi":
                translated_text = translate_to_hindi(final_summary)
                st.info(translated_text)
            else:
                st.info("Switch to Hindi for translation")

    # -----------------------------
    # Tab 3: Unfavorable Terms
    # -----------------------------
    with tabs[3]:
        st.subheader("🚨 Identification of Unfavorable Terms")
        unfavorable_terms = detect_unfavorable_terms(contract_text)

        if unfavorable_terms:
            for f in unfavorable_terms:
                st.markdown(
                    f"""
                    ---
                    ❌ **Term:** {f['term'].capitalize()}  
                    📌 **Why risky?** {f['explanation']}  
                    📄 **Context:**  
                    > {f['snippet']}
                    """
                )

            report = "\n\n".join(
                [f"{f['term'].upper()}:\n{f['explanation']}\nContext: {f['snippet']}" for f in unfavorable_terms]
            )
            st.download_button("⬇️ Download Unfavorable Terms Report", report, file_name="unfavorable_terms.txt")
        else:
            st.success("✅ No unfavorable terms detected.")