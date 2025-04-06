
    import { NgModule } from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';
    import { HttpClientModule } from '@angular/common/http';
    import { AppComponent } from './app.component';
    import { LogoComponentComponent } from './logocomponent/logocomponent.component';
import { TextFieldComponentComponent } from './textfieldcomponent/textfieldcomponent.component';
import { QrCodeComponentComponent } from './qrcodecomponent/qrcodecomponent.component';
import { NameComponentComponent } from './namecomponent/namecomponent.component';
import { DateComponentComponent } from './datecomponent/datecomponent.component';
import { ButtonComponentComponent } from './buttoncomponent/buttoncomponent.component';
import { BackgroundComponentComponent } from './backgroundcomponent/backgroundcomponent.component';

    import { DashboardServiceService } from './services/dashboardservice.service';
import { LeaveManagementServiceService } from './services/leavemanagementservice.service';
import { PodServiceService } from './services/podservice.service';
import { AuthServiceService } from './services/authservice.service';

    @NgModule({
      declarations: [
        AppComponent,
        LogoComponentComponent,
    TextFieldComponentComponent,
    QrCodeComponentComponent,
    NameComponentComponent,
    DateComponentComponent,
    ButtonComponentComponent,
    BackgroundComponentComponent,

      ],
      imports: [
        BrowserModule,
        HttpClientModule
      ],
      providers: [
    import { DashboardServiceService } from './services/dashboardservice.service';
import { LeaveManagementServiceService } from './services/leavemanagementservice.service';
import { PodServiceService } from './services/podservice.service';
import { AuthServiceService } from './services/authservice.service';

      ],
      bootstrap: [AppComponent]
    })
    export class AppModule { }
    