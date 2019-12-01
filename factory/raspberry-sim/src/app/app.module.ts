import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {DashboardComponent} from './dashboard/dashboard.component';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatCardModule} from '@angular/material/card';
import {MatMenuModule} from '@angular/material/menu';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {LayoutModule} from '@angular/cdk/layout';
import {FirstComponent} from './workstations/first/first.component';
import {SecondComponent} from './workstations/second/second.component';
import {MainComponent} from './workstations/main/main.component';
import {FlexLayoutModule} from '@angular/flex-layout';
import {PartComponent} from './shared/part/part.component';
import {ArmComponent} from './shared/arm/arm.component';
import {ApiService} from './core/service/api.service';
import {WorkstationService} from './core/service/workstation.service';
import {HttpClientModule} from '@angular/common/http';
import { LegendComponent } from './legend/legend.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    FirstComponent,
    SecondComponent,
    MainComponent,
    PartComponent,
    ArmComponent,
    LegendComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatGridListModule,
    MatCardModule,
    MatMenuModule,
    MatIconModule,
    MatButtonModule,
    LayoutModule,
    FlexLayoutModule,
    HttpClientModule
  ],
  providers: [ApiService, WorkstationService],
  bootstrap: [AppComponent]
})
export class AppModule { }
