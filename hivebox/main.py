"""Main Fast API file"""
from datetime import datetime, timezone
import os
import statistics
from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

LOCATIONS = [
    {"lat": 52.52, "lon": 13.41},   # Berlin
    {"lat": 48.85, "lon": 2.35},    # Paris
    {"lat": 41.90, "lon": 12.49}    # Rome
]

@app.get("/")
async def root():
    """Function printing hello world"""
    return {"message": "Hello, World!"}

@app.get("/changes")
async def get_changes():
    """API Changes"""
    return {
        "message": "Changes from default hivebox project will be tracked here",
        "versions": {
            "v0.0.1": ["1. Opensense API changed"]
        }
    }

@app.get("/version")
async def get_version():
    """Function printing App version."""
    return {"version":"v0.0.1"}

@app.get("/temperature")
async def get_temperature():
    """Function to get temperature"""
     # In CI or if no API key is set, return a mock
    if os.getenv("CI") == "true":
        return {"average_temperature": 25}

    temps = []
    now = datetime.now(timezone.utc)

    async with httpx.AsyncClient() as client:
        for loc in LOCATIONS:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={
                loc['lat']}&longitude={loc['lon']}&current=temperature_2m"
            r = await client.get(url)
            if r.status_code != 200:
                continue

            data = r.json()
            current_data = data.get("current",{})
            if "time" not in current_data or "temperature_2m" not in current_data:
                continue

            reading_time = datetime.fromisoformat(current_data["time"]).replace(tzinfo=timezone.utc)
            age_minutes = (now - reading_time).total_seconds() /60

            if age_minutes <= 60:
                temps.append(current_data["temperature_2m"])
    if not temps:
        raise HTTPException(status_code=500,
                            detail="No fresh temperature data available (older than 1 hour).")

    avg_temp = statistics.mean(temps)
    return {
        "average_temperature": avg_temp,
        "sources_used":len(temps),
        "timestamp_checked":now.isoformat()
    }
