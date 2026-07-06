import json
from embeddings import embed_text, cosine_similarity


def retrieve_relevant_chunks(question, index_file="index.json", top_k=3):
    with open(index_file, "r", encoding="utf-8") as f:
        index = json.load(f)

    question_vector = embed_text(question)

    scored = []
    for item in index:
        score = cosine_similarity(question_vector, item["vector"])
        scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    top_matches = scored[:top_k]

    return [item for score, item in top_matches]
