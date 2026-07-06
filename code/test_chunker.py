from loaders import extract_text_from_txt
from chunker import chunk_text

# Step 1: get the raw text
text = extract_text_from_txt("Knowledge Base/sample.txt")

# Step 2: split it into chunks
chunks = chunk_text(text)

# Step 3: see what we got
print(f"Total chunks: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)