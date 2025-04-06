
import os
from typing import Dict
from app.models.frontend_state import FrontendState

def run_command(command: str):
    """Executes a shell command and handles errors."""
    try:
        os.system(command)
    except Exception as e:
        print(f"Error executing command: {command}\n{e}")

def ensure_project_exists(project_root: str):
    """Creates an Angular project if it doesn't already exist."""
    if not os.path.exists(project_root):
        run_command(f"ng new {project_root} --skip-install --style=scss --routing --ssr=false")

def create_component(component_name: str, code: Dict[str, str]):
    """Generates an Angular component and writes the generated HTML/TS/CSS files."""
    component_path = f"src/app/{component_name.lower()}"
    os.makedirs(component_path, exist_ok=True)
    
    # Generate Angular component using CLI
    run_command(f"ng generate component {component_name.lower()}")

    # Write component files
    html_file = os.path.join(component_path, f"{component_name.lower()}.component.html")
    ts_file = os.path.join(component_path, f"{component_name.lower()}.component.ts")
    css_file = os.path.join(component_path, f"{component_name.lower()}.component.scss")

    if "html" in code:
        with open(html_file, "w") as f:
            f.write(code["html"])

    if "ts" in code:
        with open(ts_file, "a") as f:
            f.write(f"\n{code['ts']}")

    if "css" in code:
        with open(css_file, "w") as f:
            f.write(code["css"])  

def create_service(service_name: str, logic: str):
    """Generates an Angular service and writes the generated TypeScript logic."""
    service_path = "src/app/services"
    os.makedirs(service_path, exist_ok=True)

    # Generate Angular service using CLI
    run_command(f"ng generate service services/{service_name.lower()}")

    # Write service logic
    service_file = os.path.join(service_path, f"{service_name.lower()}.service.ts")
    with open(service_file, "a") as f:
        f.write(f"\n{logic}")

def update_app_module(state: FrontendState):
    """Updates the app module to include all components and services."""
    app_module_file = "src/app/app.module.ts"
    app_component_file = "src/app/app.component.html"

    # Generate imports and declarations for components
    component_imports = ""
    component_declarations = ""
    for component in state.component_code.keys():
        component_class = component + "Component"
        component_imports += f"import {{ {component_class} }} from './{component.lower()}/{component.lower()}.component';\n"
        component_declarations += f"    {component_class},\n"

    # Generate imports for services
    service_imports = ""
    for service in state.service_code.keys():
        service_class = service + "Service"
        service_imports += f"import {{ {service_class} }} from './services/{service.lower()}.service';\n"

    # Write app.module.ts
    app_module_content = f"""
    import {{ NgModule }} from '@angular/core';
    import {{ BrowserModule }} from '@angular/platform-browser';
    import {{ HttpClientModule }} from '@angular/common/http';
    import {{ AppComponent }} from './app.component';
    {component_imports}
    {service_imports}
    @NgModule({{
      declarations: [
        AppComponent,
    {component_declarations}
      ],
      imports: [
        BrowserModule,
        HttpClientModule
      ],
      providers: [
    {service_imports}
      ],
      bootstrap: [AppComponent]
    }})
    export class AppModule {{ }}
    """

    with open(app_module_file, "w") as f:
        f.write(app_module_content)

    # Update app.component.html to include all components
    app_component_html_content = "\n".join([f"<app-{component.lower()}></app-{component.lower()}>" for component in state.component_code.keys()])
    with open(app_component_file, "w") as f:
        f.write(app_component_html_content)

def generate_code(state: FrontendState) -> FrontendState:
    project_root = "GeneratedAngularApp"

    # Ensure Angular project exists
    ensure_project_exists(project_root)

    # Change directory to project
    os.chdir(project_root)

    # Generate components
    for component, code in state.component_code.items():
        create_component(component, code)

    # Generate services
    for service, logic in state.service_code.items():
        create_service(service, logic)

    # Update app module
    update_app_module(state)

    # Change back to root directory
    os.chdir("..")

    return state


