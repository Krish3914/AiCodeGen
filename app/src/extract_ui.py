
from app.models.frontend_state import FrontendState
from app.core.config import llm

from groq import Groq
import json
import re



# 1. Extract UI from Screenshot (OCR + Vision)
def extract_ui(state: FrontendState) -> FrontendState:
    # Implement OCR-based UI extraction logic

    # Getting the base64 string
    base64_image = state.path1

    client = Groq()
    Image_prompt=""""Analyze the provided image and identify all UI components present. For each component, provide the following details:

Component Type: Specify the type of UI component (e.g., button, text field, checkbox, dropdown menu, etc.).
Text Content: If the component contains text, provide the text content.
Position: Provide the position of the component within the image (e.g., coordinates or relative position).
Size: Provide the size of the component (e.g., width and height).
Color: Provide the primary color of the component.
State: If applicable, specify the state of the component (e.g., enabled, disabled, selected, etc.).

Ensure that all identified components are listed in a structured format for easy reference."""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": Image_prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model="llama-3.2-11b-vision-preview",
    )

    ui_data=chat_completion.choices[0].message.content
    cell_prompt=f"""You are an expert UI analyst. Convert the extracted UI elements into a structured JSON format that represents the component hierarchy. Ensure the JSON includes:
- The type of component (e.g., button, input, text, dropdown, etc.).
- The text inside the component (if applicable).
- The position (x, y coordinates) of the component.
- The width and height of the component.
- Any additional attributes like `placeholder`, `color`, `id`, `class`, etc.

Here’s the extracted UI data:

{ui_data}



Convert this into the following JSON format:
Expected Json format:

{{
  "components": {{
    {{
      "type": "button",
      "text": "Submit",
      "position": [100, 200],
      "size": [80, 30],
      "attributes": {{
        "id": "submit-btn",
        "class": "btn-primary",
        "color": "blue"
      }}
    }},
    {{
      "type": "input",
      "placeholder": "Enter your email",
      "position": [50, 150],
      "size": [200, 40],
      "attributes": {{
        "id": "email-input",
        "class": "form-control",
        "type": "email"
      }}
    }}
  }}
}}

Only return json object nothing else
"""
    cells=llm.invoke(cell_prompt)
    json_match=re.search(r'\{.*\}',cells.content,re.DOTALL)
    state.ui_elements=json.loads(json_match.group(0))
    state.path1="image"


    return state



