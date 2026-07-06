import os
import csv
from docx import Document
from pypdf import PdfReader


def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text


def extract_text_from_docx(file_path):
    doc = Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs]
    text = "\n".join(paragraphs)
    return text


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    pages_text = [page.extract_text() or "" for page in reader.pages]
    text = "\n".join(pages_text)
    return text


def extract_text_from_csv(file_path):
    rows_text = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_text = ", ".join(f"{key}: {value}" for key, value in row.items())
            rows_text.append(row_text)
    text = "\n".join(rows_text)
    return text


def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue
        extension = os.path.splitext(filename)[1].lower()
        if extension == ".txt" or extension == ".md":
            text = extract_text_from_txt(file_path)
        elif extension == ".docx":
            text = extract_text_from_docx(file_path)
        elif extension == ".pdf":
            text = extract_text_from_pdf(file_path)
        elif extension == ".csv":
            text = extract_text_from_csv(file_path)
        else:
            print(f"Warning: skipping unsupported file type: {filename}")
            continue
        documents.append({"source": filename, "text": text})
    return documents