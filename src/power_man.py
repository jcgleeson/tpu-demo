"""Module providing a function some shortcuts for dataclasses."""
from dataclasses import dataclass
from datetime import datetime

# NOTE: Don't use the logging class when containerized. Use prints instead
# and let Docker Compose or Kubernetes handle the logging threads.
# from logging import getLogger

# NOTE: Shouldn't need pathlib from a contiainerized app as all paths are
# relative to the container root running in a unix file system.
# import pathlib

# TO-DO: setup linters and formatters.

@dataclass
class PowerEvent:
    """
    Docstring for Location
    """
    name: str
    lat: float
    lon: float
    time: datetime

class PowerEventManager:
    """
    Docstring for LocationManager
    """
    power_events: list[PowerEvent]

    def __init__(self):
        self.power_events = []

    def add_power_event(self, power_event: PowerEvent) -> None:
        """Add a location to the manager."""
        return self.power_events.append(power_event)

    def get_power_event_by_name(self, name: str) -> PowerEvent | None:
        """Get a location by its name."""
        for locus in self.power_events:
            if locus.name == name:
                return locus
        return None

    def get_lattitudes(self) -> list[float]:
        """Get a list of all latitudes."""
        return [loc.lat for loc in self.power_events]

    def get_longitudes(self) -> list[float]:
        """Get a list of all longitudes."""
        return [loc.lon for loc in self.power_events]

    def get_names(self) -> list[str]:
        """Get a list of all location names."""
        return [loc.name for loc in self.power_events]


if __name__ == "__main__":
    power_manager = PowerEventManager()
    power_manager.add_power_event(
        PowerEvent(name="New York", lat=40.7128, lon=-74.0060, time=datetime.now())
    )
    power_manager.add_power_event(
        PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437, time=datetime.now())
    )
    for pow_event in power_manager.power_events:
        print(f"""
            Location: {pow_event.name},
            Latitude: {pow_event.lat},
            Longitude: {pow_event.lon},
            Time: {pow_event.time.strftime("%Y-%m-%d %H:%M:%S")}"""
        )
