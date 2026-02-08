import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path)
    else:
        raise ValueError("Unsupported file type")

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    return splitter.split_documents(docs)



# from langchain_community.document_loaders import PyPDFLoader, TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# import os

# def load_and_chunk(file_path: str):
#     ext = os.path.splitext(file_path)[1].lower()

#     if ext == ".pdf":
#         loader = PyPDFLoader(file_path)
#     elif ext == ".txt":
#         loader = TextLoader(file_path)
#     else:
#         raise ValueError("Unsupported file type")

#     documents = loader.load()

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=150
#     )

#     return splitter.split_documents(documents)


# import tempfile
# import os
# from langchain_community.document_loaders import PyPDFLoader, TextLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def load_and_chunk(file):
#     suffix = os.path.splitext(file.filename)[1]

#     with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
#         tmp.write(file.file.read())
#         path = tmp.name

#     loader = PyPDFLoader(path) if suffix == ".pdf" else TextLoader(path)
#     documents = loader.load()

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=150
#     )

#     chunks = splitter.split_documents(documents)
#     os.remove(path)
#     return chunks

