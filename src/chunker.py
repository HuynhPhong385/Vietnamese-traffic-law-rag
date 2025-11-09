from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80,
        separators=[
            "\nĐiều ",
            "\nKhoản ",
            "\n1. ",
            "\n2. ",
            "\n3. ",
            "\n4. ",
            "\n5. ",
            "\n6. ",
            "\n7. ",
            "\n8. ",
            "\n9. ",
            "\n",
            ". "
        ]
    )

    return splitter.split_documents(documents)