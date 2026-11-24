# ai-rag-knowledge-assistant

Production-ready RAG (Retrieval-Augmented Generation) AI assistant with local vector search & LLM orchestration 🧠📚

## Architecture
- **Document Ingestion**: Parses PDFs, Markdown, and text files.
- **Vector Indexing**: Employs local vector storage.
- **Retrieval Engine**: Performs semantic similarity search using dense embeddings.
- **LLM Orchestration**: Combines context with user prompts for accurate responses.

## Setup Instructions
```bash
git clone https://github.com/Darkshanu/ai-rag-knowledge-assistant.git
pip install langchain sentence-transformers chromadb
python main.py
```

## Python Snippet
```python
def query_rag_system(query: str, vector_db):
    docs = vector_db.similarity_search(query, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    return f"Context: {context}\nQuery: {query}"
```
