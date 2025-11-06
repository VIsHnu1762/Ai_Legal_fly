# Legal Fly 

AI-powered contract analysis: classify, extract clauses, assess risks, compare versions, and generate professional PDF reports.

## Quick Start
```bash
# 1) Setup
./setup.sh            # auto install & init DB
# or
pip install -r requirements.txt && python init_db.py

# 2) Run UI (Streamlit)
streamlit run app_pro.py   # http://localhost:8501

# 3) Run API (FastAPI)
python api/main.py         # http://localhost:8000/docs

# 4) Demo / One-liner
./demo.sh                  # guided tour
python3 quickstart.py      # quick launch
```

## Core Features
- 11 contract type classification (ensemble NLP)
- 15+ risk pattern detection with severity scoring
- Clause extraction (16 clause categories + importance)
- Contract comparison & risk deltas
- Multi-language translation (6+ languages)
- Persisted analyses (SQLAlchemy + SQLite)
- PDF report generation (summary, risks, clauses)
- REST API + interactive docs (Swagger)

## Minimal Structure
```
contract/
  app_pro.py        # Streamlit app
  api/main.py       # FastAPI server
  database/         # ORM models & connection
  utils/            # AI modules (classifier, risk, clauses)
  reports/          # PDF generator
  demo.sh / setup.sh / quickstart.py
  START_HERE.md     # Extended guide
```

## Key API Endpoints
```
POST /api/v1/contracts/analyze        # upload & analyze PDF
GET  /api/v1/contracts/{id}           # retrieve analysis
GET  /api/v1/contracts/{id}/report    # download PDF
POST /api/v1/contracts/compare        # compare two contracts
GET  /api/v1/contracts                # list all analyses
```

## Troubleshooting
```bash
pip install -r requirements.txt --upgrade    # deps
python -m spacy download en_core_web_sm      # missing model
python init_db.py                            # recreate DB
lsof -ti:8501 | xargs kill                   # free Streamlit port
lsof -ti:8000 | xargs kill                   # free API port
```

## Performance & Security (Highlights)
- Caching + lazy model load for speed
- SHA-256 file hashing & ORM safety
- Audit-ready persistent records

## Roadmap (Next)
- Auth & roles, custom risk rules, templates

## Legal Disclaimer
This software provides informational AI analysis only and is not legal advice. Consult a qualified attorney for decisions.

## More Docs
See `START_HERE.md` for full guide, `WHATS_NEW.md` for upgrade details.

## Get Started
```bash
./demo.sh
streamlit run app_pro.py
```

Version 2.0.0 • 2025
