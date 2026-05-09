# AI Document Analyzer

An AI-powered document analysis application that allows users to upload PDF documents and interact with them using natural language queries. The system uses Retrieval-Augmented Generation (RAG), embeddings, vector databases, and Large Language Models (LLMs) to provide intelligent answers based on document content.

---

## Features

- Upload and analyze PDF documents
- Ask questions about uploaded documents
- AI-powered contextual responses
- Semantic search using embeddings
- Vector database integration using FAISS
- Streamlit frontend for interactive UI
- FastAPI backend for API handling
- Supports multiple document types and large PDFs
- Real-time document querying

---

## Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI
- Uvicorn

### AI / ML
- LangChain
- Sentence Transformers
- FAISS Vector Database
- LLM Integration

### Other Libraries
- PyPDF
- NumPy


---

## Project Architecture

```text
User Uploads PDF
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
FAISS Vector Storage
        ↓
Similarity Search
        ↓
LLM Response Generation
        ↓
Answer Displayed to User
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI-Document-Analyzer.git
```

### Move into Project Folder

```bash
cd AI-Document-Analyzer
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Backend

Move to backend folder:

```bash
cd backend
```

Start FastAPI server:

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

# Running the Frontend

Open another terminal.

Move to frontend folder:

```bash
cd frontend
```

Run Streamlit:

```bash
streamlit run app.py
```

Frontend runs at:

```text
http://localhost:8501
```

---

## Example Questions

- Summarize this document
- What are the key skills mentioned?
- Extract important dates
- Explain the main topic
- What technologies are discussed?
- Generate a short overview

---

## Future Improvements

- Multi-document support
- Chat history
- Authentication system
- Cloud deployment
- OCR support for scanned PDFs
- Advanced document summarization
- Voice interaction

---

## Deployment

### Frontend
- Streamlit Community Cloud

### Backend
- Render / Railway / AWS

