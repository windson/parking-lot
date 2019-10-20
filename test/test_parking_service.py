import unittest
from service.park_service import EntryService
from models.car import Car

class park_service_tests(unittest.TestCase):
    
    def test_entry(self):
        car = Car('KA-01-HH-1234', 'White')
        park_svc = EntryService()
        park_svc.allow(car)
        #self.assertEqual("d","d")
        #self.assertEqual(park_svc.enter('KA-01-HH-1234', 'White'), True)
        

    
