import unittest
from service.park_service import park_service

class park_service_tests(unittest.TestCase):
    def test_entry(self):
        park_svc = park_service()
        self.assertEqual(park_svc.enter('KA-01-HH-1234', 'White'), True)
    
    if __name__ == 'main':
        unittest.main()