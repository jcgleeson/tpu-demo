"""Tests for loc_man module."""
from power_man import PowerEventManager, PowerEvent


class TestLocMan:
    """
    Let's test the LocationManager class and its methods.
    """
    def test_get_location_by_name(self):
        """
        Docstring for test_get_location_by_name
        
        :param self: Description
        """
        loc_manager = PowerEventManager()
        loc_manager.add_location(PowerEvent(name="New York", lat=40.7128, lon=-74.0060))
        loc_manager.add_location(PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437))
        assert loc_manager.get_location_by_name("New York") == PowerEvent(name="New York", lat=40.7128, lon=-74.0060)
        assert loc_manager.get_location_by_name("Los Angeles") == PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437)
        assert loc_manager.get_location_by_name("Chicago") is None

    def test_get_lattitudes(self):
        """
        Docstring for test_get_lattitudes
        
        :param self: Description
        """
        loc_manager = PowerEventManager()
        loc_manager.add_location(PowerEvent(name="New York", lat=40.7128, lon=-74.0060))
        loc_manager.add_location(PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437))
        assert loc_manager.get_lattitudes() == [40.7128, 34.0522]

    def test_get_longitudes(self):
        """
        Docstring for test_get_longitudes
        
        :param self: Description
        """
        loc_manager = PowerEventManager()
        loc_manager.add_location(PowerEvent(name="New York", lat=40.7128, lon=-74.0060))
        loc_manager.add_location(PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437))
        assert loc_manager.get_longitudes() == [-74.006, -118.2437]

    def test_get_names(self):
        """
        Docstring for test_get_names
        
        :param self: Description
        """
        loc_manager = PowerEventManager()
        loc_manager.add_location(PowerEvent(name="New York", lat=40.7128, lon=-74.0060))
        loc_manager.add_location(PowerEvent(name="Los Angeles", lat=34.0522, lon=-118.2437))
        assert loc_manager.get_names() == ["New York", "Los Angeles"]
