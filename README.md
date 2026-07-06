# Knowledge Base Assistant

## Overview

Knowledge Base Assistant is a Retrieval-Augmented Generation (RAG) system that answers user questions using only the documents stored in a local knowledge base.

The application processes multiple document formats, converts them into semantic embeddings using Google Gemini, stores them in a local vector index, retrieves the most relevant content based on semantic similarity, and generates accurate responses using Google's Gemini Large Language Model.

The system is designed to minimize hallucinations by restricting responses to the retrieved context only.

## Features

- Multi-format document support (PDF, DOCX, TXT, Markdown, CSV)
- Automatic document ingestion from a `Knowledge Base` folder
- Paragraph-based document chunking
- Semantic embeddings using Google Gemini's embedding model
- Local vector index with cosine similarity search
- Google Gemini integration for answer generation
- Hallucination prevention through strict context grounding
- Graceful handling of unsupported file types
- Modular project architecture

## Technologies Used

- Python 3.13
- [google-genai](https://pypi.org/project/google-genai/) — Google Gemini SDK (embeddings + generation)
- `pypdf` — PDF text extraction
- `python-docx` — DOCX text extraction
- `python-dotenv` — environment variable management
- Built-in `csv` and `json` modules for CSV parsing and local vector storage

## Project Structure

```
TASK1/
├── Knowledge Base/          # Place documents here (pdf, docx, txt, md, csv)
├── code/
│   ├── loaders.py           # File-type extractors + document dispatcher
│   ├── chunker.py           # Splits document text into chunks
│   ├── embeddings.py        # Gemini embedding calls + cosine similarity
│   ├── build_index.py       # Builds the local vector index (index.json)
│   ├── retriever.py         # Retrieves top matching chunks for a question
│   └── assistant.py         # Main entry point — RAG question answering
├── .env                     # API key (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/heshamyehya19/TASK1.git
   cd TASK1
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project root with your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

You can generate a key at [Google AI Studio](https://aistudio.google.com/apikey).

**Note:** Never commit your `.env` file. It is already listed in `.gitignore`.

## How to Run

1. Add your documents (PDF, DOCX, TXT, MD, or CSV) to the `Knowledge Base` folder in the project root.

2. Build the index (run this once, and again any time you add or change documents):

   ```
   python code/build_index.py
   ```

   This reads all supported files, splits them into chunks, generates embeddings, and saves everything to `index.json`.

3. Run the assistant:
   ```
   python code/assistant.py
   ```
   You'll be prompted to type a question. The assistant retrieves the most relevant chunks from your knowledge base and generates an answer using Gemini, grounded strictly in that content.

## Usage Example

```
python code/assistant.py

Ask me a question: How many annual leave days do employees get?

Answer: Employees have 21 annual leave days per year.
```

```
Ask me a question: What is the CEO's salary?

Answer: I don't have that information in the knowledge base.
```

## Assumptions and Limitations

- The assistant only reads files placed directly inside the `Knowledge Base` folder; subfolders are not scanned.
- PDF extraction works on text-based PDFs; scanned/image-only PDFs without a text layer will not extract any content.
- Documents are chunked by paragraph (split on blank lines). Very long paragraphs are not further split, and documents with unusual formatting (e.g. inconsistent spacing) may chunk imperfectly.
- The vector index (`index.json`) is stored locally as a flat file rather than in a dedicated vector database, which is suitable for small-to-medium knowledge bases but would not scale efficiently to very large document collections.
- The index must be manually rebuilt (`python code/build_index.py`) after adding or changing documents; there is no automatic file-watching.
- This implementation is a CLI tool. A web-based interface was not required for this submission but could be added as a Flask/FastAPI layer on top of the existing `assistant.py` logic.
