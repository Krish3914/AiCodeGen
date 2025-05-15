
    import { NgModule } from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';
    import { HttpClientModule } from '@angular/common/http';
    import { AppComponent } from './app.component';
    import { HeaderComponentComponent } from './headercomponent/headercomponent.component';
import { LabelComponentComponent } from './labelcomponent/labelcomponent.component';
import { TextFieldComponentComponent } from './textfieldcomponent/textfieldcomponent.component';
import { PasswordFieldComponentComponent } from './passwordfieldcomponent/passwordfieldcomponent.component';
import { ButtonComponentComponent } from './buttoncomponent/buttoncomponent.component';
import { IconComponentComponent } from './iconcomponent/iconcomponent.component';
import { DashboardComponentComponent } from './dashboardcomponent/dashboardcomponent.component';
import { LeaveManagementSystemComponentComponent } from './leavemanagementsystemcomponent/leavemanagementsystemcomponent.component';
import { PodsComponentComponent } from './podscomponent/podscomponent.component';
import { LoginFormComponentComponent } from './loginformcomponent/loginformcomponent.component';

    import { AuthServiceService } from './services/authservice.service';
import { LeaveServiceService } from './services/leaveservice.service';
import { PodServiceService } from './services/podservice.service';

    @NgModule({
      declarations: [
        AppComponent,
        HeaderComponentComponent,
    LabelComponentComponent,
    TextFieldComponentComponent,
    PasswordFieldComponentComponent,
    ButtonComponentComponent,
    IconComponentComponent,
    DashboardComponentComponent,
    LeaveManagementSystemComponentComponent,
    PodsComponentComponent,
    LoginFormComponentComponent,

      ],
      imports: [
        BrowserModule,
        HttpClientModule
      ],
      providers: [
    import { AuthServiceService } from './services/authservice.service';
import { LeaveServiceService } from './services/leaveservice.service';
import { PodServiceService } from './services/podservice.service';

      ],
      bootstrap: [AppComponent]
    })
    export class AppModule { }
    