
    import { NgModule } from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';
    import { HttpClientModule } from '@angular/common/http';
    import { AppComponent } from './app.component';
    import { HeaderComponentComponent } from './headercomponent/headercomponent.component';
import { LoginFormComponentComponent } from './loginformcomponent/loginformcomponent.component';
import { DashboardComponentComponent } from './dashboardcomponent/dashboardcomponent.component';

    import { AuthServiceService } from './services/authservice.service';
import { LeaveServiceService } from './services/leaveservice.service';
import { PodServiceService } from './services/podservice.service';

    @NgModule({
      declarations: [
        AppComponent,
        HeaderComponentComponent,
    LoginFormComponentComponent,
    DashboardComponentComponent,

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
    