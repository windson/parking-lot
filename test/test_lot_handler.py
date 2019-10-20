import unittest
from service.lot_handler import LotHandler
from models.slot import Slot

class test_lot_handler(unittest.TestCase):
    
    def test_lot_handler_initalize(self):
        lh = LotHandler(6)
        self.assertEqual(lh.capacity, 6)
        self.assertEqual(len(lh.slots), 6)
        for i in range(0,6):
            self.assertTrue(lh.slots[i].IsAvailable)
