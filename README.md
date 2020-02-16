## Problem Statement
FULLStack OpenTheme 10

Amalgamation of Weather Forecast from multiple free public data streams & APIs (Yahoo weather, Accu-weather, ForecastIo, Weather Underground, Aeris-weather, Open-weather Map etc.& many more. A more detailed list can be furnished later) & amalgamate these through some statistical averaging to produce a single integrated weather forecast stream for a particular geo location within a certain Km radius. We would like to provide this information on our App & also publish an API if​ possible.




## What I have built

MauSUM - a weather application which aggregrates data from multiple sources and gives most accurate weather data. It hits various external apis from a backend in Python/Flask, aggregates there data and generate final result as consumable REST API. Frontend built in Angular 7 access the API and displays result in intuitive manner.


## Technologies Used

- Python Flask 
    - Hit various API through HTTP, requests module
    - Independent API

- Angular 7
    - Async fetches data using obervable subscriber pattern
    - process & modification of data in UI

- HTML/CSS/Bootstrap
    - simple yet powerful

- APIs Used
    - OpenWeatherMap
    - DarkSky
    - SimpleMaps : to get indian city coordinates


## Challenges
- Breaking down problem and decide MVP Feature (mentors helped to figure out MUST HAVE Feature)
- Variation in format of different data sources (created custom weather class and SI Unit convertion function)

## Future Modification

- Caching of API responses
- Integrating Google Maps Autocomplete place API
- Weather data from more sources
- API Authentication & Throttling
- Error handling, logging & docs 
