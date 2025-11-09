from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from src.loader import load_all_documents
from src.chunker import split_documents


VECTOR_DB_PATH = "vector_store/faiss_index"


def build_vector_store():
    print("Loading documents...")
    docs = load_all_documents()

    print("Chunking documents...")
    chunks = split_documents(docs)

    print(f"Total chunks: {len(chunks)}")

    print("Loading embedding model...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    print("Creating FAISS index...")
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    print("Saving vector DB...")
    vectorstore.save_local(VECTOR_DB_PATH)

    print("Done!")
    print(f"Saved to: {VECTOR_DB_PATH}")


if __name__ == "__main__":
    build_vector_store()