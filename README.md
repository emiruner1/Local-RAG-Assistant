# Local RAG Assistant

A privacy-focused local AI assistant that uses **Retrieval-Augmented Generation (RAG)** to answer questions from PDF documents without requiring documents to be sent to a remote AI service.

## Overview

Local RAG Assistant allows users to upload PDF documents, process their contents, retrieve relevant information, and generate context-aware answers using a locally running language model.

The project combines document processing, semantic retrieval, SQLite-based storage, and local AI inference into a simple RAG pipeline.

## How It Works

```text
PDF Document
     ↓
Text Extraction
     ↓
Text Chunking
     ↓
Embeddings
     ↓
SQLite Storage
     ↓
Relevant Context Retrieval
     ↓
Local LLM
     ↓
Generated Answer
```

## Features

* 📄 PDF document ingestion
* 🔎 Retrieval-Augmented Generation (RAG)
* 🧩 Text chunking and semantic retrieval
* 🗄️ SQLite-based local storage
* 🤖 Local LLM inference
* 🔐 Privacy-focused architecture
* 💬 Question answering over uploaded documents
* 🌐 Local web interface

## Project Structure

```text
Local-RAG-Assistant/
│
├── database/
│   └── sqlite_manager.py
│
├── rag/
│   ├── embeddings.py
│   ├── ingest.py
│   ├── llm.py
│   ├── prompt.py
│   └── retrieval.py
│
├── templates/
│   └── index.html
│
├── ui/
│   └── streamlit_app.py
│
├── utils/
│   ├── chunker.py
│   └── pdf_loader.py
│
├── app.py
├── config.py
└── requirements.txt
```

## Technologies

* Python
* Retrieval-Augmented Generation (RAG)
* Microsoft Foundry Local
* SQLite
* PyPDF
* Embeddings
* Flask
* Streamlit

## Installation

Clone the repository:

```bash
git clone https://github.com/emiruner1/Local-RAG-Assistant.git
cd Local-RAG-Assistant
```

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Start the local application with:

```bash
python app.py
```

The application will be available locally at:

```text
http://127.0.0.1:5000
```

## Usage

1. Open the local application in your browser.
2. Upload a PDF document.
3. Wait for the document to be processed.
4. Enter a question related to the uploaded document.
5. The RAG pipeline retrieves relevant context.
6. The local language model generates an answer based on the retrieved information.

## Privacy

The project is designed around local processing. Documents can remain on the user's machine instead of being uploaded to an external AI service.

> Do not commit private documents, API keys, passwords, `.env` files, databases, or other sensitive information to the repository.

## Project Status

This project is under active development. Future improvements may include improved retrieval quality, conversation history, richer document support, source highlighting, and an enhanced user interface.

## License

This project is currently provided for educational and development purposes.
