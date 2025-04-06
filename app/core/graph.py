from langgraph.graph import StateGraph
from app.models.frontend_state import FrontendState
from app.src.extract_ui import extract_ui
from app.src.extract_srs import extract_srs
from app.src.generate_angular_code import generate_angular_code
from app.src.generate_structure import generate_code
from app.src.generate_documentations import generate_documentation
from dotenv import load_dotenv
import os
from langgraph.checkpoint.memory import MemorySaver
load_dotenv()
os.environ['LANGSMITH_API_KEY']=os.getenv("LANGSMITH_API_KEY")
os.environ['LANGSMITH_ENDPOINT']=os.getenv("LANGSMITH_ENDPOINT")
os.environ['LANGSMITH_TRACING']="true"




graph = StateGraph(FrontendState)

graph.add_node("extract_ui", extract_ui)
graph.add_node("extract_srs", extract_srs)
graph.add_node("generate_angular_code", generate_angular_code)
graph.add_node("generate_structure", generate_code)
graph.add_node("generate_documentation", generate_documentation)


graph.add_edge("extract_ui", "extract_srs")
graph.add_edge("extract_srs", "generate_angular_code")
graph.add_edge("generate_angular_code", "generate_structure")
graph.add_edge("generate_structure", "generate_documentation")

graph.set_entry_point("extract_ui")
graph.set_finish_point("generate_documentation")
memory=MemorySaver()
compiled_graph = graph.compile(checkpointer=memory)

print(compiled_graph.get_graph().draw_mermaid())




