from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_faiss(texts):
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embeddings

def retrieve(query, texts, index):
    q_emb = model.encode([query])
    _, idx = index.search(q_emb, k=5)
    return [texts[i] for i in idx[0]]
