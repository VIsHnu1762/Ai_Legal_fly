# reader.py
import pdfplumber
import pytesseract
from pdf2image import convert_from_path

def read_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for i, page in enumerate(pdf.pages, start=1):
                page_text = page.extract_text()
                if page_text:
                    text += f"[Page {i}]\n{page_text}\n"
    except Exception as e:
        print("Error reading with pdfplumber:", e)

    if not text.strip():
        print("No text found, using OCR...")
        images = convert_from_path(file_path)
        for i, img in enumerate(images, start=1):
            text += f"[Page {i} OCR]\n{pytesseract.image_to_string(img)}\n"

    return text