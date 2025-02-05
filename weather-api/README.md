weather-api/
├── app/
│   ├── __init__.py
│   ├── main.py        # Entry point for the FastAPI ap
│   ├── schemas.py     # Pydantic models for validation
│   ├── db.py          # Database connection setup
│   └── services/
│       └── weather_service.py  # Business logic (OOP)
├── tests/             # Unit tests
└── README.md          # Documentation

Create new project **weather-api**
Create new package **app**
1. Install FastAPI and Uvicorn
  - pip install fastapi uvicorn
2. Run FastAPI sing the Terminal
  - uvicorn app.main:app --reload
3. Open the browser: `http://127.0.0.1:8000/`
4. Run Uvicorn with Network Binding
  - uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


## How to add data (POST)
1. Create a json file. Sample:
rmionescu@raspberry:~/scripts/weather-api$ cat weather_data.json
{
  "location": "Bucuresti",
  "temperature": 5.2,
  "humidity": 80,
  "condition": "Cloudy"
}

2. Run: curl -X POST "http://192.168.1.191:8000/weather/" -H "Content-Type: application/json" -d @weather_data.json
3. Response
{"location":"Bucuresti","temperature":5.2,"humidity":80.0,"condition":"Cloudy","id":2,"timestamp":"2025-02-03T11:56:22.584490"}

## Fetch data (GET)
1. All locations:
  - url: http://192.168.1.191:8000/weather/

[
{
      "location": "Bucuresti",
      "temperature": 4.8,
      "humidity": 75.0,
      "condition": "Cloudy",
      "id": 1,
      "timestamp": "2025-02-03T11:56:22.584490"
},
{
      "location": "Bucuresti",
      "temperature": 5.2,
      "humidity": 80.0,
      "condition": "Cloudy",
      "id": 2,
      "timestamp": "2025-02-03T11:56:22.584490"
}
]
2. For a specific location
  - curl: curl -X GET 'http://192.168.1.191:8000/weather/?location=Brasov' -H 'accept: application/json'
3. Fetch the average temperature for current month (require a location)
  - url: http://192.168.1.191:8000/weather/average/?location=Brasov
  - curl: curl -X GET "http://192.168.1.191:8000/weather/average/?location=Brasov" -H 'accept: application/json'
4. Fetch the max temperature all time (require a location)
  - url: http://192.168.1.191:8000/weather/max/?location=Brasov
  - curl: curl -X GET "http://192.168.1.191:8000/weather/max/?location=Brasov" -H 'accept: application/json'

## Delete data (DELETE)
1. Delete data using id
  - curl: curl -X DELETE "http://192.168.1.191:8000/weather/5"