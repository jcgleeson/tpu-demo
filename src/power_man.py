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
    locations: list[PowerEvent]

    def __init__(self):
        self.locations = []

    def add_location(self, location: PowerEvent) -> None:
        """Add a location to the manager."""
        return self.locations.append(location)

    def get_location_by_name(self, name: str) -> PowerEvent | None:
        """Get a location by its name."""
        for locus in self.locations:
            if locus.name == name:
                return locus
        return None

    def get_lattitudes(self) -> list[float]:
        """Get a list of all latitudes."""
        return [loc.lat for loc in self.locations]

    def get_longitudes(self) -> list[float]:
        """Get a list of all longitudes."""
        return [loc.lon for loc in self.locations]

    def get_names(self) -> list[str]:
        """Get a list of all location names."""
        return [loc.name for loc in self.locations]


if __name__ == "__main__":
    loc_manager = PowerEventManager()
    loc_manager.add_location(PowerEvent(name="New York", lat=40.7128, lon=-74.0060))
    loc_manager.add_location(PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437))
    for loc in loc_manager.locations:
        print(f"Location: {loc.name}, Latitude: {loc.lat}, Longitude: {loc.lon}")
