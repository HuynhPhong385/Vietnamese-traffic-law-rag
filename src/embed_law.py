from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from src.loader import load_documents
from src.chunker import split_documents

VECTOR_DB_PATH = "vector_store/law_index"

LAW_FILES = [
    "23_2008_QH12_82203.docx",
    "Quy định xử phạt vi phạm hành chính trong lĩnh vực giao thông đường bộ và đường sắt (01).pdf",
    "Quy định xử phạt vi phạm hành chính trong lĩnh vực giao thông đường bộ và đường sắt (02).pdf",
]

def build():
    print("Loading law documents...")
    docs = load_documents(allowed_files=LAW_FILES)

    print("Chunking...")
    chunks = split_documents(docs)

    print("Embedding...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    print("Building FAISS...")
    db = FAISS.from_documents(chunks, embeddings)

    print("Saving...")
    db.save_local(VECTOR_DB_PATH)

    print("Done.")  

if __name__ == "__main__":
    build()