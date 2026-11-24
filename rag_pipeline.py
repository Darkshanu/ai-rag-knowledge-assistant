import os

def query_rag(query: str):
    print(f"Querying RAG system: {query}")
    return "Sample RAG Response"

if __name__ == "__main__":
    print(query_rag("What is MCP?"))
