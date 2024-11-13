from langchain_ollama import OllamaEmbeddings

def get_embedding_function() -> OllamaEmbeddings:
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    return embeddings