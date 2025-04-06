
from pydantic import BaseModel
from typing import Dict, List,Any

class FrontendState(BaseModel):
    path1: str = ""
    path2: str = ""
    ui_elements: Dict[Any, Any] = {}
    srs_details: Dict[Any, Any] = {}
    component_code: Dict[Any, Any] = {}
    service_code: Dict[Any, Any] = {}
    module_code: str = ""
    error_logs: List[str] = []

