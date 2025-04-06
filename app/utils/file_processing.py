
import base64
from langchain_community.document_loaders import Docx2txtLoader

def process_ui(image_path):
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    base64_image = encode_image(image_path)
    return {"base64_image": base64_image}

def process_docs(docs_path):
    loader = Docx2txtLoader(docs_path)
    data = loader.load()
    return {"srs_details": data[0].page_content}


