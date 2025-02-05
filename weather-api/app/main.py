from fastapi import FastAPI, HTTPException
from app.db import initialize_db
from app import schemas
from app.services.weather_service import WeatherService

app = FastAPI()
weather_service = WeatherService()

# Initialize the database when the app starts
initialize_db()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather API!"}


@app.post("/weather/", response_model=schemas.WeatherResponse)
def create_weather(weather: schemas.WeatherCreate):
    return weather_service.create_weather(weather)


@app.get("/weather/", response_model=list[schemas.WeatherResponse])
def get_weather(location: str = None):
    return weather_service.get_weather(location)


@app.get("/weather/average/")
def get_average(location: str):
    return weather_service.get_average(location)


@app.get("/weather/max/")
def get_max(location: str):
    return weather_service.get_max(location)


@app.delete("/weather/{weather_id}")
def delete_weather(weather_id: int):
    weather = weather_service.delete_weather(weather_id)
    if not weather:
        raise HTTPException(status_code=404, detail="Weather data not found")
    return {"message": "Weather data deleted successfully"}
