import { Component, OnInit } from '@angular/core';
import { WeatherService } from './weather.service';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css']
})
export class WeatherComponent implements OnInit {

  constructor(public wService: WeatherService) { }

  ngOnInit() {
    // this.getData(18.52, 73.85);
    this.getCities();
  }

  data = "";
  CITIES = {};
  currentDateTime = new Date();
  temperature = 0;
  pressure = 0;
  humidity = 0;
  future = [];
  condition = "";
  icon = "";
  selectedCity = "";

  getCities(){
    this.wService.getAllCities().subscribe(
      resp =>{
        this.CITIES = resp;
      })
  }

  getData(lt, ln){
    this.wService.getCurrentWeather(lt, ln).subscribe(
      resp => {
        console.log(resp);
        this.data = resp;
        this.future = resp["future"];
      },
      err =>{

      }
    )
  }

  cityChange(){
    let lat = this.selectedCity["lat"];
    let lon = this.selectedCity["lng"];
    this.getData(lat, lon);
  }



}
