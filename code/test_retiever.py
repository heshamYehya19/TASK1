from retriever import retrieve_relevant_chunks

results = retrieve_relevant_chunks("How many leave days do employees get?")
for r in results:
    print(r["source"], "-", r["text"][:80])
