import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BsDropdownModule } from 'ngx-bootstrap/dropdown';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NgbPaginationModule, NgbAlertModule } from '@ng-bootstrap/ng-bootstrap';
import { DropdownComponent } from './dropdown/dropdown.component';
import { ProfileimageComponent } from './profileimage/profileimage.component';
import { GenerateContentComponent } from './generate-content/generate-content.component';
import { HttpClientModule } from '@angular/common/http';



@NgModule({
  declarations: [ 
    AppComponent, DropdownComponent, ProfileimageComponent, GenerateContentComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    BsDropdownModule.forRoot(),
    NgbModule,
    NgbPaginationModule,
    NgbAlertModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
