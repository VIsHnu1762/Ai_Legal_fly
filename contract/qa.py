#qa
# qa.py
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def answer_question(question, context):
    return qa_pipeline(question=question, context=context)["answer"]
def chunk_text(text, chunk_size=3000):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i+chunk_size])

summary_texts = []
for chunk in chunk_text(contract_text):
    summary_chunk = summary(chunk, max_length=200, min_length=50, do_sample=False)
    summary_texts.append(summary_chunk[0]['summary_text'])

final_summary = " ".join(summary_texts)
print(final_summary)