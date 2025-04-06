
from app.core.config import llm
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
from langchain_huggingface import HuggingFaceEmbeddings
import re



def agentGenerator(input:str)->str:
    connection = "postgresql+psycopg2://admin:admin@localhost:5432/langchain_db"  # Uses psycopg3!
    collection_name = "my_vector_store"
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    import psycopg2

    vector_store = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True)
    searched=vector_store.similarity_search(input)
    data=""
    for i in searched:
        data+=(i.page_content)

    prompt = (
        f"Given the following query: '{input}', generate only the Python code for an agent. "
        f"You can find the help of the agent in the documentation provided.'{data}'"
        "Do not include any explanations or additional text. The code should be self-contained and functional."
    )
    
    response=llm.invoke(prompt)
    
    content_stripped = re.sub(r'```python\n|```', '', response.content).strip()
    print(response.content)

    with open("generated_agent.py", "w", encoding="utf-8") as f:
        f.write(content_stripped)
    return "Agent created check your folder for generated_agent.py"


#check


