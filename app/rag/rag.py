
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
from langchain_huggingface import HuggingFaceEmbeddings


connection = "postgresql+psycopg2://admin:admin@localhost:5432/langchain_db"  # Uses psycopg3!
collection_name = "my_vector_store"

file_path="doc\Employee Handbook .pdf"
pages=[]
for i in range(1,5):
    doc_path = f"doc\{i}.pdf"
    loader = PyPDFLoader(doc_path)
    for page in loader.alazy_load():
        pages.append(page)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(pages)

all_splits_text=[chunk.page_content for chunk in all_splits]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

import psycopg2
vector_store = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)


data=vector_store.add_texts(texts=all_splits_text)


