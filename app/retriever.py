from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer('all-MiniLM-L6-v2')

def search_clauses(query, index, embeddings, chunks, k=3):
    query_vec = model.encode([query])
    D, I = index.search(np.array(query_vec, dtype=np.float32), k)
    return [chunks[i] for i in I[0]]
