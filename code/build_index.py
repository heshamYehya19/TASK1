import json
from loaders import load_documents
from chunker import chunk_text
from embeddings import embed_text


def build_index(folder_path="Knowledge Base", output_file="index.json"):
    documents = load_documents(folder_path)
    index = []

    for doc in documents:
        chunks = chunk_text(doc["text"])
        for chunk in chunks:
            vector = embed_text(chunk)
            index.append({
                "source": doc["source"],
                "text": chunk,
                "vector": vector
            })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(index, f)

    print(f"Indexed {len(index)} chunks from {len(documents)} documents.")


if __name__ == "__main__":
    build_index()
