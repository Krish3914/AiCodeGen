
from langchain_groq import ChatGroq
import json
import re
from app.models.frontend_state import FrontendState
from app.core.config import llm


def extract_srs(state: FrontendState) -> FrontendState:

    extracted_srs_data=state.path2
    prompt = f"""
    You are an expert in software architecture and requirements engineering. Convert the extracted Software Requirements Specification (SRS) into a structured JSON format.

    ### Extracted SRS Data:
    {extracted_srs_data}

    ### Expected JSON format:
    {{
      "requirements": [
        "User should be able to submit a form",
        "Application should fetch user details from the backend",
        "Login system with JWT authentication"
      ],
      "components": [
        {{
          "name": "LoginForm",
          "type": "form",
          "fields": [
            {{"name": "email", "type": "text", "validation": "required"}},
            {{"name": "password", "type": "password", "validation": "required"}}
          ],
          "buttons": [
            {{"text": "Login", "action": "submit"}}
          ]
        }},
        {{
          "name": "Dashboard",
          "type": "container",
          "elements": ["Navbar", "Sidebar", "MainContent"]
        }}
      ],
      "api_endpoints": [
        {{
          "name": "Get User Details",
          "method": "GET",
          "url": "/api/user/details",
          "response": {{
            "id": "number",
            "name": "string",
            "email": "string"
          }}
        }},
        {{
          "name": "User Login",
          "method": "POST",
          "url": "/api/auth/login",
          "request": {{
            "email": "string",
            "password": "string"
          }},
          "response": {{
            "token": "string",
            "expires_in": "number"
          }}
        }}
      ],
      "dependencies": [
        "Angular 15",
        "RxJS",
        "Bootstrap",
        "TailwindCSS"
      ]
    }}

    Only return the JSON output, nothing else.
    """
    cells=llm.invoke(prompt)
    json_match=re.search(r'\{.*\}',cells.content,re.DOTALL)
    state.srs_details=json.loads(json_match.group(0))
 
   
    return state


