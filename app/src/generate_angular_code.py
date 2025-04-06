
from app.models.frontend_state import FrontendState
from app.core.config import llm
import json
import re

def generate_angular_code(state: FrontendState) -> FrontendState:
    """
    Generates Angular components and services based on UI elements and SRS details.
    Stores the results in `state.component_code` and `state.service_code`.
    """

    # Ensure UI elements and SRS details exist
    ui_elements = json.dumps(state.ui_elements, indent=2)
    srs_details = json.dumps(state.srs_details, indent=2)

    # 📌 Prompt for generating Angular code
    prompt = f"""
    You are an expert Angular developer. Based on the UI elements and Software Requirements Specification (SRS), generate Angular SCSS, TypeScript, and HTML code.

    ### **UI Elements:**
    {ui_elements}

    ### **SRS Details:**
    {srs_details}

    ### **Expected Output:**
    - JSON object with **components** containing TypeScript, HTML, and SCSS code.
    - JSON object with **services** containing TypeScript logic for API calls.
    - Ensure that all components and services are properly integrated into the Angular application.
    - Include necessary imports and module declarations to make the application fully functional.

    ### **Example Output:**

    ```json
    {{
      "component_code": {{
        "Loginform": {{
          "html": "<form> <input type='email' placeholder='Email'> <input type='password' placeholder='Password'> <button>Login</button> </form>",
          "ts": "import {{ Component }} from '@angular/core'; @Component({{ selector: 'app-login', templateUrl: './login.component.html', styleUrls: ['./login.component.scss'] }}) export class LoginComponent {{ }}",
          "css": "form {{ display: flex; flex-direction: column; }} input {{ margin-bottom: 10px; }} button {{ background-color: blue; color: white; }}"
        }},
        "Dashboard": {{
          "html": "<div>Welcome to Dashboard</div>",
          "ts": "import {{ Component }} from '@angular/core'; @Component({{ selector: 'app-dashboard', templateUrl: './dashboard.component.html', styleUrls: ['./dashboard.component.scss'] }}) export class DashboardComponent {{ }}",
          "css": "div {{ font-size: 20px; color: green; }}"
        }}
      }},
      "service_code": {{
        "AuthService": "import {{ Injectable }} from '@angular/core'; import {{ HttpClient }} from '@angular/common/http'; @Injectable({{ providedIn: 'root' }}) export class AuthService {{ constructor(private http: HttpClient) {{}} login(user: any) {{ return this.http.post('/api/auth/login', user); }} }}"
      }},
      "module_code": "import {{ NgModule }} from '@angular/core'; import {{ BrowserModule }} from '@angular/platform-browser'; import {{ HttpClientModule }} from '@angular/common/http'; import {{ AppComponent }} from './app.component'; import {{ LoginComponent }} from './login/login.component'; import {{ DashboardComponent }} from './dashboard/dashboard.component'; import {{ AuthService }} from './services/auth.service'; @NgModule({{ declarations: [AppComponent, LoginComponent, DashboardComponent], imports: [BrowserModule, HttpClientModule], providers: [AuthService], bootstrap: [AppComponent] }}) export class AppModule {{ }}"
    }}
    ```

    Only return the JSON output, nothing else.
    """

    # 📌 Call LLM to generate Angular code
    cells = llm.invoke(prompt)
    json_match = re.search(r'\{.*\}', cells.content, re.DOTALL)
    output_json = json.loads(json_match.group(0))

    # Extract JSON output   
    state.component_code = output_json.get("component_code", {})
    state.service_code = output_json.get("service_code", {})
    state.module_code = output_json.get("module_code", "")
    print(state.component_code)
    print("/n /n /n /n /n/n n/n /n/n")
    print(state.service_code)
    print(state.module_code)

    return state


