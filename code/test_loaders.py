from loaders import load_documents

docs = load_documents("Knowledge Base")
for doc in docs:
    print(doc["source"], "->", len(doc["text"]), "characters")