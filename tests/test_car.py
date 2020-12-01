import unittest
from unittest.mock import *
from Car import Car

class TestCar(unittest.TestCase):
    def setUp(self):
        self.temp = Car()

    def test_needs_fuel_true(self):
        self.temp.needs_fuel = Mock(name='needs_fuel')
        self.temp.needs_fuel.return_value = True
        self.assertEqual(self.temp.needs_fuel(), True)

    def test_needs_fuel_false(self):
        self.temp.needs_fuel = Mock(name='needs_fuel')
        self.temp.needs_fuel.return_value = False
        self.assertEqual(self.temp.needs_fuel(), False)

    @patch.object(Car, 'get_engine_temperature')
    def test_get_engine_temperature(self, mock_method):
        mock_method.return_value = 45
        result = self.temp.get_engine_temperature()
        self.assertEqual(result, 45)

    @patch.object(Car, 'drive_to_destination')
    def test_drive_to_destination(self, mock_method):
        destination = 'Maroko'
        mock_method.return_value = 'Drive to {}'.format(destination)
        result = self.temp.drive_to_destination(destination)
        self.assertEqual(result, 'Drive to {}'.format(destination))
