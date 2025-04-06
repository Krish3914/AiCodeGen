from fastapi import APIRouter, UploadFile, File
from app.core.graph import compiled_graph
from app.utils.file_processing import process_ui, process_docs
from pydantic import BaseModel
from app.rag.agentGenerator import agentGenerator

router = APIRouter()
class QueryRequest(BaseModel):
    query: str

@router.post("/generate-agent-code", response_model=str)
async def generate_agent_code(request: QueryRequest):
    query = request.query
    return agentGenerator(query)


@router.post("/upload/")
async def extract_ui_and_docs(ui_file: UploadFile = File(...), docs_file: UploadFile = File(...)):
    # ui_path = f"temp/{ui_file.filename}"
    # docs_path = f"temp/{docs_file.filename}"
    ui_path = "files/image1.png"
    docs_path = "files/SRD frontend.docx"
    
    with open(ui_path, "wb") as f:
        f.write(await ui_file.read())
    
    with open(docs_path, "wb") as f:
        f.write(await docs_file.read())
    
    ui_elements = process_ui(ui_path)
    srs_details = process_docs(docs_path)
    
    empty_input = {
        "path1": ui_elements["base64_image"],
        "path2": srs_details["srs_details"],
        "ui_elements": {},
        "srs_details": {},
        "component_code": {},
        "service_code": {},
        "test_code": {},
        "documentation": "",
        "error_logs": [],
        "module_code": ""
    }
    config={"configurable":{"thread_id":1}}
    output = compiled_graph.invoke(empty_input,config=config)
    return output


