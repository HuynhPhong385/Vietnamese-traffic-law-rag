from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader

DOCS_DIR = "documents"

def load_documents(allowed_files=None):
    docs = []

    for file in Path(DOCS_DIR).iterdir():
        if allowed_files and file.name not in allowed_files:
            continue

        suffix = file.suffix.lower()

        try:
            if suffix == ".pdf":
                print(f"Loading PDF: {file.name}")
                docs.extend(PyPDFLoader(str(file)).load())

            elif suffix == ".docx":
                print(f"Loading DOCX: {file.name}")
                docs.extend(Docx2txtLoader(str(file)).load())

        except Exception as e:
            print(f"ERROR loading {file.name}: {e}")

    return docs