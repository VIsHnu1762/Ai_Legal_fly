# ⚖️ Legal Fly Pro 

**Legal Fly** is an **AI-powered contract intelligence platform** that analyzes legal contract PDFs to classify their type, extract key clauses, assess risks (with severity), compare document versions, and generate professional PDF reports.

It includes both:
- 🌐 A **web UI (Streamlit)** for non-technical users  
- ⚙️ A **REST API (FastAPI)** for developers and system integration

---

## 🧭 What It Is

Legal Fly Pro helps automate the tedious process of **contract review, risk assessment, and reporting** using advanced NLP and rule-based intelligence.

---

## 👥 Who It’s For

- **Individuals** reviewing employment, rental, or service agreements  
- **Small businesses** screening vendor and partnership contracts  
- **Legal teams** triaging documents, prioritizing risks, and reporting to clients  

---

## ⚡ What It Does

### 🧩 Core Capabilities

| Capability | Description |
|-------------|-------------|
| **Contract Classification** | Identifies **11+ contract types** using an ensemble of NLP models |
| **Risk Analysis** | Detects **15+ risk patterns** with `Critical / High / Medium / Low` severity and recommendations |
| **Clause Extraction** | Finds and scores **16 clause categories** (e.g., Termination, Confidentiality, Indemnity) |
| **Comparison** | Highlights differences and **risk deltas** between two contracts |
| **Reporting** | Generates clean, branded **PDF reports** with summaries, findings, and visuals |
| **History** | Stores analyses for quick retrieval and auditing |
| **Multi-Language** | Provides summaries and insights in **6+ languages** via on-the-fly translation |

---

## 🧠 How It Works (High Level)

1. **Upload** – Provide a contract PDF via the Streamlit app or API.  
2. **Analyze** – The system extracts text, classifies the contract, finds clauses, and scores risks.  
3. **Store** – Results are saved in the database for history and re-use.  
4. **Act** – Download a professional PDF report, compare versions, or integrate through REST endpoints.

---

## 🏗️ Architecture at a Glance

| Component | Description |
|------------|-------------|
| **UI** | Streamlit app (`app_pro.py`) with interactive visuals and analysis tabs |
| **API** | FastAPI service (`main.py`) with Swagger documentation for easy integration |
| **AI Modules** | Classifier, Risk Analyzer, Clause Extractor (`utils/`) |
| **Reports** | PDF Generator (`pdf_generator.py`) using ReportLab / fpdf2 |
| **Database** | SQLAlchemy ORM with **SQLite** (default, can be swapped for Postgres/MySQL) |

---

## 💪 Key Strengths

- ✅ **Accurate & Explainable** — Ensemble of NLP + rule-based models  
- ⚙️ **Production-Ready** — Database-backed, API-enabled, and report-exportable  
- 🧩 **Extensible** — Add new risk rules, clause types, and contract categories easily  
- 🌍 **For All Users** — Designed for both **end users (UI)** and **developers (API)**  

---

## 🔁 Typical Workflow

1. 📄 Upload a contract PDF  
2. 🧠 Review detected **contract type and confidence score**  
3. 🚨 Inspect **risk findings** and severity levels  
4. 📑 Explore extracted **clauses and key terms**  
5. 🧾 Generate and download a **professional PDF report**  
6. 🔍 (Optional) **Compare** with another contract version and save results  

---

## 🧰 Tech Stack

| Layer | Tools / Libraries |
|--------|-------------------|
| **Backend** | Python, FastAPI |
| **Frontend (UI)** | Streamlit |
| **Database** | SQLAlchemy (SQLite default) |
| **NLP / AI** | spaCy, Transformers, Sentence-Transformers |
| **PDF Generation** | ReportLab / fpdf2 |

---

## 📈 Status & Roadmap

| Version | Stage | Key Notes |
|----------|--------|-----------|
| **v2.0.0** | ✅ Stable | Core features, API, reporting, and history implemented |
| **v2.1.0 (Next)** | 🚧 Planned | Authentication & roles, custom risk rules, templates, deeper integrations |

---

## ⚙️ Setup (For Developers)

```bash
# Clone the repository
git clone https://github.com/<your-username>/Legal_Fly_Pro.git
cd Legal_Fly_Pro

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
## ▶️ Run Locally:
Run Streamlit UI:
```
streamlit run app_pro.py
```
Run FastAPI server:
```
uvicorn main:app --reload
```
Access the UI at 👉 http://localhost:8501
Access the API docs at 👉 http://localhost:8000/docs

