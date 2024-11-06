from langchain_ollama import OllamaEmbeddings

def get_embedding_function() -> OllamaEmbeddings:
    embeddings = OllamaEmbeddings(model="llama3.2")
    return embeddings