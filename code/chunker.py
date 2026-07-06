def chunk_text(text, min_length=20):
    paragraphs = text.split("\n\n")
    chunks = [p.strip() for p in paragraphs if len(p.strip()) >= min_length]
    return chunks