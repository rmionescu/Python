from pydantic import BaseModel
from datetime import datetime


class WeatherCreate(BaseModel):
    location: str
    temperature: float
    humidity: float
    condition: str


class WeatherResponse(WeatherCreate):
    id: int
    timestamp: datetime
