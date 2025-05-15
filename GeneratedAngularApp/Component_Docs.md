# Angular Components Documentation
## Overview
This documentation provides an in-depth look at the Angular components used in the application. It covers the properties, state management, and API integration details for each component.

### 1. HeaderComponent
#### Properties
* `title`: The title of the header
* `logo`: The logo of the application
* `navItems`: An array of navigation items

#### State Management
* The component uses a service to fetch the navigation items from the API
* The service is injected into the component using dependency injection

#### API Integration
* The component uses the `NavigationService` to fetch the navigation items
* The `NavigationService` makes a GET request to the `/nav-items` endpoint to retrieve the navigation items

#### Example Usage
```html
<app-header [title]="'My Application'" [logo]="'logo.png'" [navItems]="navItems"></app-header>
```

### 2. LabelComponent
#### Properties
* `text`: The text to be displayed
* `styleType`: The style of the label (e.g. 'primary', 'secondary')

#### State Management
* The component uses a simple state management approach, where the text and style are bound to the component's properties

#### API Integration
* None

#### Example Usage
```html
<app-label [text]="'Hello World'" [styleType]="'primary'"></app-label>
```

### 3. TextFieldComponent
#### Properties
* `label`: The label of the text field
* `placeholder`: The placeholder text of the text field
* `value`: The value of the text field
* `type`: The type of the text field (e.g. 'text', 'email')

#### State Management
* The component uses a form control to manage the state of the text field
* The form control is bound to the component's properties

#### API Integration
* None

#### Example Usage
```html
<app-text-field [label]="'Username'" [placeholder]="'Enter username'" [value]="'johnDoe'" [type]="'text'"></app-text-field>
```

### 4. PasswordFieldComponent
#### Properties
* `label`: The label of the password field
* `placeholder`: The placeholder text of the password field
* `value`: The value of the password field

#### State Management
* The component uses a form control to manage the state of the password field
* The form control is bound to the component's properties

#### API Integration
* None

#### Example Usage
```html
<app-password-field [label]="'Password'" [placeholder]="'Enter password'" [value]="'password123'"></app-password-field>
```

### 5. ButtonComponent
#### Properties
* `text`: The text to be displayed on the button
* `styleType`: The style of the button (e.g. 'primary', 'secondary')
* `disabled`: A boolean indicating whether the button is disabled

#### State Management
* The component uses a simple state management approach, where the text and style are bound to the component's properties

#### API Integration
* None

#### Example Usage
```html
<app-button [text]="'Submit'" [styleType]="'primary'" [disabled]="false"></app-button>
```

### 6. IconComponent
#### Properties
* `iconName`: The name of the icon
* `styleType`: The style of the icon (e.g. 'primary', 'secondary')

#### State Management
* The component uses a simple state management approach, where the icon name and style are bound to the component's properties

#### API Integration
* None

#### Example Usage
```html
<app-icon [iconName]="'user'" [styleType]="'primary'"></app-icon>
```

### 7. DashboardComponent
#### Properties
* `widgets`: An array of widgets to be displayed on the dashboard

#### State Management
* The component uses a service to fetch the widgets from the API
* The service is injected into the component using dependency injection

#### API Integration
* The component uses the `WidgetService` to fetch the widgets
* The `WidgetService` makes a GET request to the `/widgets` endpoint to retrieve the widgets

#### Example Usage
```html
<app-dashboard [widgets]="widgets"></app-dashboard>
```

### 8. LeaveManagementSystemComponent
#### Properties
* `leaveTypes`: An array of leave types
* `leaveBalances`: An array of leave balances

#### State Management
* The component uses a service to fetch the leave types and leave balances from the API
* The service is injected into the component using dependency injection

#### API Integration
* The component uses the `LeaveService` to fetch the leave types and leave balances
* The `LeaveService` makes a GET request to the `/leave-types` and `/leave-balances` endpoints to retrieve the leave types and leave balances

#### Example Usage
```html
<app-leave-management-system [leaveTypes]="leaveTypes" [leaveBalances]="leaveBalances"></app-leave-management-system>
```

### 9. PodsComponent
#### Properties
* `pods`: An array of pods

#### State Management
* The component uses a service to fetch the pods from the API
* The service is injected into the component using dependency injection

#### API Integration
* The component uses the `PodService` to fetch the pods
* The `PodService` makes a GET request to the `/pods` endpoint to retrieve the pods

#### Example Usage
```html
<app-pods [pods]="pods"></app-pods>
```

### 10. LoginFormComponent
#### Properties
* `username`: The username of the user
* `password`: The password of the user

#### State Management
* The component uses a form control to manage the state of the username and password
* The form control is bound to the component's properties

#### API Integration
* The component uses the `AuthenticationService` to authenticate the user
* The `AuthenticationService` makes a POST request to the `/login` endpoint to authenticate the user

#### Example Usage
```html
<app-login-form [username]="'johnDoe'" [password]="'password123'"></app-login-form>
```

Note: The above documentation is a general outline and may need to be modified based on the specific requirements of your application.