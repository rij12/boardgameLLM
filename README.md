# LangChain 

Ask questions about board games such as monopoly.

## Build 

1. Setups Python3 venv
2. Install requirements.txt to venv
3. Creates ChromaDB 

```bash
make init
```

## Run

```bash
make run q="YOUR QUERY"
```


## Design 

![alt text](https://python.langchain.com/assets/images/rag_indexing-8160f90a90a33253d0154659cf7d453f.png)


1. Load: First we need to load our data. This is done with Document Loaders.
2. Split: Text splitters break large Documents into smaller chunks. This is useful both for indexing data and passing it into a model, as large chunks are harder to search over and won't fit in a model's finite context window.
3. Store: We need somewhere to store and index our splits, so that they can be searched over later. This is often done using a VectorStore and Embeddings model.

## Model Card 

For: 
* Embbeding function
* LLM model 

https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md 