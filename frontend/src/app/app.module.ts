import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { WeatherComponent } from './weather/weather.component';
import { TempConvPipe } from './weather/temp-conv.pipe';

@NgModule({
  declarations: [
    AppComponent,
    WeatherComponent,
    TempConvPipe
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
