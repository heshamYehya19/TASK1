from google import genai
from retriever import retrieve_relevant_chunks
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def answer_question(question, top_k=3):
    print("DEBUG - question repr:", repr(question))
    chunks = retrieve_relevant_chunks(question, top_k=top_k)

    context = "\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}" for c in chunks)

    prompt = f"""You are a knowledge base assistant. Answer the question using ONLY the context below.
If the answer is not contained in the context, respond exactly with: "I don't have that information in the knowledge base."
Do not make up or assume any information that isn't explicitly stated in the context.

Context:
{context}

Question: {question}

Answer:"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    question = input("ASK ME A QUESTION: ")
    answer = answer_question(question)
    print("\nAnswer:", answer)
