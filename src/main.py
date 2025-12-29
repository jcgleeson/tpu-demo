"""
Quick rest api for the power manager.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from power_man import PowerEventManager

app = FastAPI()
pow_manager = PowerEventManager()

class PowerEvent(BaseModel):
    """
    Docstring for PowerEvent
    """
    name: str
    lat: float
    lon: float


@app.get("/")
async def root():
    """
    Docstring for root
    """
    print("Root endpoint called.")
    return {"message": "Root of Power Manager API"}

@app.post("/add_event/")
async def add_event(event: PowerEvent):
    """
    Docstring for add_event
    
    :param event_name: Description
    :type event_name: str
    """
    print(f"Received event: {event}")
    json_str = event.model_dump_json()
    pow_manager.add_power_event_json(json_str)
    return {"message": f"Event {event.name} added successfully."}
