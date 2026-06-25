# AI Study Assistant

## Overview

AI Study Assistant is a Retrieval-Augmented Generation (RAG) application built with FastAPI, LangChain, FAISS, and Mistral AI. Users can upload PDF documents and ask questions about their content. The system retrieves relevant information from the uploaded documents and generates structured educational responses.

---

## Features

### PDF Processing

* Upload PDF documents
* Extract text using PyMuPDF
* Automatically split documents into chunks

### Semantic Search

* Generate embeddings using Hugging Face models
* Store embeddings in FAISS vector database
* Retrieve relevant content using similarity search

### AI-Powered Question Answering

* Uses Mistral AI for response generation
* Answers based only on uploaded documents
* Reduces hallucinations through Retrieval-Augmented Generation (RAG)

### Structured Responses

Each answer contains:

* Topic Title
* Definition
* Explanation
* Examples

---

## Project Structure

```text
AI_Study_Assistant/
│
├── app/
│   ├── api/
│   │   ├── upload.py
│   │   └── chat.py
│   │
│   ├── services/
│   │   ├── pdf_loader.py
│   │   ├── chunker.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── llm.py
│   │   └── rag.py
│   │
│   ├── schemas/
│   │   └── study_response.py
│   │
│   └── main.py
│
├── uploads/
├── vector_db/
├── .env
├── requirements.txt
└── README.md
```

---

## Technology Stack

### Backend

* FastAPI
* Uvicorn

### AI & NLP

* LangChain
* Mistral AI
* Hugging Face Embeddings

### Vector Database

* FAISS

### Document Processing

* PyMuPDF

### Validation

* Pydantic

---

## Installation

Clone the repository:

```bash
git clone https://github.com/maroofiums/AI_Study_Assistant.git
cd AI_Study_Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Upload PDF

**POST**

```text
/upload
```

Upload a PDF document for processing and indexing.

Response:

```json
{
  "message": "PDF uploaded successfully",
  "chunks": 42
}
```

---

### Ask Questions

**GET**

```text
/chat?query=What is gradient descent?
```

Response:

```json
{
  "topic_title": "Gradient Descent",
  "definition": "An optimization algorithm used to minimize a loss function.",
  "explanation": "It updates parameters in the opposite direction of the gradient.",
  "examples": [
    "Linear Regression",
    "Logistic Regression",
    "Neural Networks"
  ]
}
```

---

## RAG Pipeline

```text
User Uploads PDF
        │
        ▼
PyMuPDF Loader
        │
        ▼
Text Chunking
        │
        ▼
Embeddings Generation
        │
        ▼
FAISS Vector Store
        │
        ▼
User Question
        │
        ▼
Retriever
        │
        ▼
Relevant Context
        │
        ▼
Mistral AI
        │
        ▼
Structured Response
```

---

## Future Improvements

### Phase 2

* User Authentication (JWT)
* PostgreSQL Database
* Multiple PDFs per User
* Chat History
* Document Management

### Phase 3

* Quiz Generation
* Flashcard Generation
* Automatic Summaries
* Learning Progress Tracking

### Phase 4

* React Frontend
* Docker Deployment
* CI/CD Pipeline
* Cloud Deployment

---

## Learning Outcomes

This project demonstrates:

* FastAPI Development
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Prompt Engineering
* Large Language Model Integration
* Structured AI Outputs
* Production-Ready API Design

---

## License

This project is available for educational and portfolio purposes.
