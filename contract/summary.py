# summary.py
from transformers import pipeline

summarizer = pipeline("summarization", model="google/bigbird-pegasus-large-arxiv")

def chunk_text(text, chunk_size=1000):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i+chunk_size])

def summarize_contract(contract_text):
    summary_chunks = []
    for chunk in chunk_text(contract_text):
        chunk_summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
        summary_chunks.append(chunk_summary[0]['summary_text'])

    combined_summary = " ".join(summary_chunks)
    final = summarizer(combined_summary, max_length=250, min_length=80, do_sample=False)[0]['summary_text']

    structured = []
    for line in final.split(". "):
        if line.strip():
            structured.append(f"• {line.strip()}")
    return "\n".join(structured)