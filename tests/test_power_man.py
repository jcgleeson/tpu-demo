"""Tests for power_man module."""
import unittest
from datetime import datetime
from src.power_man import PowerEventManager, PowerEvent


class TestPowerMan(unittest.TestCase):
    """
    Let's test the PowerEventManager class and its methods.
    """
    def test_get_power_event_by_name(self):
        """
        Docstring for test_get_power_event_by_name
        
        :param self: Description
        """
        power_manager = PowerEventManager()
        power_manager.add_power_event(
            PowerEvent(name="New York", lat=40.7128, lon=-74.0060, time=datetime.now())
        )
        power_manager.add_power_event(
            PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437, time=datetime.now())
        )
        self.assertEqual(power_manager.get_power_event_by_name("New York").name, "New York")
        self.assertEqual(power_manager.get_power_event_by_name("Los Angeles").name, "Los Angeles")
        self.assertIsNone(power_manager.get_power_event_by_name("Chicago"))

    def test_get_lattitudes(self):
        """
        Docstring for test_get_lattitudes
        
        :param self: Description
        """
        power_manager = PowerEventManager()
        power_manager.add_power_event(
            PowerEvent(name="New York", lat=40.7128, lon=-74.0060, time=datetime.now())
        )
        power_manager.add_power_event(
            PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437, time=datetime.now())
        )
        self.assertEqual(power_manager.get_lattitudes(), [40.7128, 34.0522])

    def test_get_longitudes(self):
        """
        Docstring for test_get_longitudes
        
        :param self: Description
        """
        power_manager = PowerEventManager()
        power_manager.add_power_event(
            PowerEvent(name="New York", lat=40.7128, lon=-74.0060, time=datetime.now())
        )
        power_manager.add_power_event(
            PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437, time=datetime.now())
        )
        self.assertEqual(power_manager.get_longitudes(), [-74.006, -118.2437])

    def test_get_names(self):
        """
        Docstring for test_get_names
        
        :param self: Description
        """
        power_manager = PowerEventManager()
        power_manager.add_power_event(
            PowerEvent(name="New York", lat=40.7128, lon=-74.0060, time=datetime.now())
        )
        power_manager.add_power_event(
            PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437, time=datetime.now())
        )
        self.assertEqual(power_manager.get_names(), ["New York", "Los Angeles"])

    def test_add_power_event_json(self):
        """
        Docstring for test_add_power_event_json
        
        :param self: Description
        """
        input_str = """
        {
            "name": "test event",
            "lat": 34.5,
            "lon": -118.5
        }
        """
        power_man = PowerEventManager()
        power_man.add_power_event_json(input_str)
        self.assertEqual(power_man.get_names(), ["test event"])
