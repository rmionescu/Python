from fastapi import HTTPException
from app.db import get_db_cursor
from app import schemas
import datetime


class WeatherService:
    @staticmethod
    def create_weather(weather_data: schemas.WeatherCreate):

        # Data validation
        if weather_data.humidity < 0 or weather_data.humidity > 100:
            raise HTTPException(status_code=422, detail="Humidity must be in range 0..100!")
        if weather_data.temperature < -100 or weather_data.temperature > 100:
            raise HTTPException(status_code=422, detail="Temperature must be in range -100..100!")

        with get_db_cursor() as cursor:
            current_date_time = datetime.datetime.now()
            sql_query = ("INSERT INTO weather (location, temperature, humidity, condition, timestamp) "
                         "VALUES (?, ?, ?, ?, ?)")
            cursor.execute(sql_query, (weather_data.location, weather_data.temperature, weather_data.humidity,
                                       weather_data.condition, current_date_time))

            weather_id = cursor.lastrowid

            # Fetch the newly added record to return it
            weather = cursor.execute("SELECT * FROM weather WHERE id = ?", (weather_id,)).fetchone()
            return dict(weather)

    @staticmethod
    def get_weather(location: str = None):
        with get_db_cursor() as cursor:

            if location:
                weather_data = cursor.execute("SELECT * FROM weather WHERE location = ?", (location,)).fetchall()
            else:
                weather_data = cursor.execute("SELECT * FROM weather").fetchall()

            return [dict(row) for row in weather_data]

    @staticmethod
    def get_average(location: str):
        with get_db_cursor() as cursor:
            sql_query = ("SELECT AVG(w.temperature), COUNT(*) "
                         "FROM weather w "
                         "WHERE location = ? AND strftime('%Y-%m', w.timestamp) = strftime('%Y-%m', 'now');")
            result = cursor.execute(sql_query, (location,)).fetchone()

            # Handle case where no data exists for the location
            if result[0] is None:
                raise HTTPException(status_code=404, detail="No weather data found for this location!")

            # Return the result in the expected JSON format
            return {"current month average": result[0], "entries": result[1]}

    @staticmethod
    def get_max(location: str):
        with get_db_cursor() as cursor:
            sql_query = "SELECT MAX(temperature) as max_temp, timestamp FROM weather WHERE location = ?"
            result = cursor.execute(sql_query, (location,)).fetchone()

            if result[0] is None:
                raise HTTPException(status_code=404, detail="No weather data found for this location!")

            return {"max temperature": result[0], "date": result[1]}

    @staticmethod
    def delete_weather(weather_id: int):
        with get_db_cursor() as cursor:
            # Check if record exists
            weather = cursor.execute("SELECT * FROM weather WHERE id = ?", (weather_id,)).fetchone()

            if weather:
                cursor.execute("DELETE FROM weather WHERE id = ?", (weather_id,))

            return dict(weather) if weather else None
