# 🧠 Legal Document Reader & Analysis AI

An intelligent **AI-powered system** designed to **read, understand, and analyze legal documents** — whether in **PDF** or **image** format.  
It identifies **flaws, inconsistencies, or risky clauses** within legal agreements and provides **context-aware insights** for lawyers, firms, and individuals.

---

## 🚀 Overview

The **Legal Document Reader & Analysis AI** leverages a **custom lightweight LLM** (Large Language Model) fine-tuned for legal text comprehension.  
It helps users automatically extract, interpret, and validate clauses from legal documents with high accuracy and efficiency.

Key Capabilities:
- 🧾 Reads legal documents from **PDFs or images**  
- 🕵️ Detects **flaws, inconsistencies, and missing clauses**  
- 🧠 Uses a **compact, domain-specific LLM** for fast local analysis  
- 💬 Generates **detailed summaries and risk assessments**  
- 🔒 Ensures **data privacy** — no external API calls required

---

## ⚙️ Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Backend** | Python |
| **Framework** | FastAPI / Flask (depending on implementation) |
| **AI / ML** | Custom-trained LLM, ONNX Runtime |
| **Computer Vision** | OpenCV, Pillow |
| **Data Handling** | NumPy, PyMuPDF, pdfplumber |
| **Frontend (optional)** | Streamlit / React (if UI is included) |

---

## 🧩 Features

- **Document Upload**: Upload PDF or scanned image documents.  
- **OCR Integration**: Extract text from non-editable image-based documents.  
- **Clause Analysis**: Identify weak or missing clauses.  
- **Risk Detection**: Highlight ambiguous or unfair contract terms.  
- **Context Summary**: Generate concise document summaries.  
- **Local Execution**: Works offline with lightweight models.

---

## 🧱 Project Structure
```
legal-document-ai/
├── app/
│   ├── main.py
│   ├── model/
│   │   └── llm_engine.py
│   ├── utils/
│   │   └── parser.py
│   └── routes/
│       └── analysis.py
├── requirements.txt
├── README.md
└── samples/
└── example_contract.pdf
```
---

## ⚡ Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/legal-document-ai.git
cd legal-document-ai
```
# Create virtual environment
```
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
# Install dependencies
```
pip install -r requirements.txt
```

