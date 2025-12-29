"""Module providing a function some shortcuts for dataclasses."""
from dataclasses import dataclass
from datetime import datetime
import json

# NOTE: Don't use the logging class when containerized. Use prints instead
# and let Docker Compose or Kubernetes handle the logging threads.
# from logging import getLogger

# NOTE: Shouldn't need pathlib from a contiainerized app as all paths are
# relative to the container root running in a unix file system.
# import pathlib

# TO-DO: setup linters, coverage checks, and formatters.

class JsonConversion(Exception):
    """Custom exception for converting json to power event."""


@dataclass
class PowerEvent:
    """
    Docstring for PowerEvent
    """
    name: str
    lat: float
    lon: float
    time: datetime

class PowerEventManager:
    """
    Docstring for PowerEventManager
    """
    # Could create a special list class and implement custom pre-sorting using
    # collections.UserList if needed.
    power_events: list[PowerEvent]

    def __init__(self):
        self.power_events = []

    def add_power_event(self, power_event: PowerEvent) -> None:
        """Add a power event to the manager."""
        return self.power_events.append(power_event)

    def add_power_event_json(self, power_event: str) -> None:
        """
        Docstring for add_power_event_json
        
        :param self: Description
        :param power_event: Description
        :type power_event: str
        :return: Description
        :rtype: bool
        """
        # NOTE: This exception handling is demonstrational. Normally would exclude and let
        # the api service handle the schema guarantees.
        try:
            # attempt to create a dict of the input json str.
            pow_event_dict = json.loads(power_event)
            if "name" not in pow_event_dict:
                raise JsonConversion("missing name from input json str!")

            pow_event_dict.update({"time": datetime.now()})

            return self.add_power_event(
                PowerEvent(
                    name=pow_event_dict["name"],
                    lat=pow_event_dict["lat"],
                    lon=pow_event_dict["lon"],
                    time=pow_event_dict["time"]
                )
            )
        except Exception as ex:
            # NOTE: if you want to keep this handler, run it and force a few exceptions
            # to get rid of the generic exception. Otherwise, this could mask other
            # failures.
            print(f"WARNING: EXCEPTION: {ex}")

    def get_power_event_by_name(self, name: str) -> PowerEvent | None:
        """Get a power event by its name (assumes names are unique)."""
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
        """Get a list of all power event names."""
        return [loc.name for loc in self.power_events]

    def get_names_iter(self) -> iter:
        """Get an iterator of all power event names."""
        for power_event in self.power_events:
            yield power_event.name


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
