import { Injectable } from '@angular/core';
import { Observable, of} from 'rxjs';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})

export class WeatherService {

  constructor(private http: HttpClient) { }

  json = { "condition": "clear sky", "future": [ { "temp": 26.16, "time": 1581791400 }, { "temp": 26.63, "time": 1581877800 }, { "temp": 27.11, "time": 1581964200 }, { "temp": 26.86, "time": 1582050600 }, { "temp": 26.38, "time": 1582137000 }, { "temp": 26.69, "time": 1582223400 }, { "temp": 26.81, "time": 1582309800 }, { "temp": 27.57, "time": 1582396200 } ], "humidity": 10.7, "icon": "01d", "latitude": "18.52", "longitude": "73.85", "pressure": 1014.6, "temperature": 304.25, "time": 1581836031.771455 };
  
  getCurrentWeather(latitude, longitude): Observable<any> {
    console.log(latitude, longitude)
    // return of(this.json);
    let url = 'http://127.0.0.1:8000/weather?latitude='+latitude+'&longitude='+longitude;
    return this.http.get(url);
  } 

  getAllCities(): Observable<any> {
      return this.http.get('./../../assets/json/in.json');
  }
}
