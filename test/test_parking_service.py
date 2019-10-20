import unittest
from service.park_service import ParkService, EntryService, ExitService
from models.car import Car

class park_service_tests(unittest.TestCase):
    
    def test_entry(self):
        #car = Car('KA-01-HH-1234', 'White')
        s = EntryService()
        s.InitializeParkingLot(6)
        with self.assertRaises(Exception) as ex:
            s.InitializeParkingLot(6)
        self.assertEqual('Already Initialized Parking Lot', str(ex.exception))
        