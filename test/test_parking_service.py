import unittest
from service.park_service import ParkService, EntryService, ExitService
from models.car import Car
from models.slot import Slot
from unittest.mock import MagicMock
from util.constants import *

class park_service_tests(unittest.TestCase):
    
    def test_re_initParkingLot_raises_Exception(self):
        # Arrange
        s = EntryService()
        s.InitializeParkingLot(6)
        
        # Act 
        # Re initialize Parking lot throws exception
        with self.assertRaises(Exception) as ex:
            s.InitializeParkingLot(6)

        # Assert
        self.assertEqual('Already Initialized Parking Lot', str(ex.exception))
        
    def test_init_parking_lot(self):
        # Arrange
        s = EntryService()

        # Act
        status, _ = s.InitializeParkingLot(6)
        
        # Assert
        self.assertEqual(status,'Created a parking lot with 6 slots')
        
    def test_init_parking_lot_raise_error_by_exit_service(self):
        # Arrange
        s = ExitService()
        
        # Act
        with self.assertRaises(AttributeError) as ex:
            s.InitializeParkingLot(6)

        # Assert
        self.assertEqual(ExitServiceCantInit, str(ex.exception))
    
    def test_allow_entry_none(self):
        # Arrange
        s = EntryService()
        s.InitializeParkingLot(6)
        
        # Act
        with self.assertRaises(Exception) as ex:
            s.allow(None)
        
        # Assert
        self.assertEqual(InvalidInput, str(ex.exception))

    def test_allow_entry_parking_lot_full(self):
        # Arrange
        car = Car('KA-01-HH-1234', 'White')
        s = EntryService()
        s.InitializeParkingLot(6)
        s.lotHandler.IsLotFull = MagicMock(return_value = True)
        
        # Act
        status = s.allow(car)

        # Assert
        self.assertEqual(status, 'Sorry, parking lot is full')
        
    def test_allow_re_park_car(self):
        # Arrange
        car = Car('KA-01-HH-1234', 'White')
        s = EntryService()
        s.InitializeParkingLot(6)
        s.lotHandler.IsCarParked = MagicMock(return_value = True)
        
        # Act
        status = s.allow(car)
        
        # Assert
        self.assertEqual('Cannot park already Parked Car: {0}'.format(car.RegNum), status)


    def test_allow_slot_unavailable(self):
        # Arrange
        car = Car('KA-01-HH-1234', 'White')
        s = EntryService()
        s.InitializeParkingLot(6)
        s.lotHandler.IsCarParked = MagicMock(return_value = False)
        s.lotHandler.IsLotFull = MagicMock(return_value = False)
        s.lotHandler.GetNearestSlot = MagicMock(return_value = 1)
        s.lotHandler.IsSlotAvailable = MagicMock(return_value = False)
        
        # Act
        with self.assertRaises(ValueError) as ex:
            s.allow(car)
        
        # Assert
        self.assertEqual('Slot Not Available'.format(car.RegNum), str(ex.exception))



    def test_allow_park_car(self):
        # Arrange
        car = Car('KA-01-HH-1234', 'White')
        s = EntryService()
        s.InitializeParkingLot(6)
        s.lotHandler.IsCarParked = MagicMock(return_value = False)
        s.lotHandler.IsLotFull = MagicMock(return_value = False)
        s.lotHandler.GetNearestSlot = MagicMock(return_value = 1)
        s.lotHandler.IsSlotAvailable = MagicMock(return_value = True)

        slot = Slot(1)
        s.lotHandler.FillSlot = MagicMock(return_value = slot)
        
        # Act
        status = s.allow(car)
        
        # Assert
        self.assertEqual(status, 'Allocated slot number: {0}'.format(1))



    def test_allow_exit_handler_initialized(self):
        # Arrange
        s = ExitService()
        
        # Act
        status = s.IsInitialized
        
        # Assert
        self.assertFalse(status)


    def test_allow_exit_none(self):
        # Arrange
        s = ExitService()
        
        # Act
        with self.assertRaises(ValueError) as ex:
            s.allow(None)
        
        # Assert
        self.assertEqual(InvalidInput, str(ex.exception))

    def test_allow_exit_UnkownError(self):
        # Arrange
        s = ExitService()
        
        # Act
        with self.assertRaises(Exception) as ex:
            s.allow(1)
        
        # Assert
        self.assertEqual(UnknownErrorOccured, str(ex.exception))

    def test_allow_exit_a_already_free_parking_lot(self):
        # Arrange
        s = ExitService()
        s.lotHandler = MagicMock(return_value = object)
        s.lotHandler.IsSlotAvailable = MagicMock(return_value = True)
        
        # Act
        with self.assertRaises(ValueError) as ex:
            s.allow(1)

        # Assert
        self.assertEqual(SlotAlreadyFree.format(1), str(ex.exception))
      

    def test_allow_exit_vaccate(self):
        # Arrange
        s = ExitService()
        s.lotHandler = MagicMock(return_value = object)
        s.lotHandler.IsSlotAvailable = MagicMock(return_value = False)
        
        # Act
        status = s.allow(1)

        # Assert
        self.assertEqual(SlotFreed.format(1), status)
      
    def test_Reg_nums_by_color(self):
        s = EntryService()
        s.InitializeParkingLot(4)
        s.lotHandler.GetRegNumsByColor = MagicMock(return_value = ['KA-01-HH-1234', 'KA-01-HH-9999', 'KA-01-P-333'])
        status = s.RegNumsByColor('Orange')
        self.assertEqual(status, 'KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333')

    def test_slot_nums_by_color(self):
        s = EntryService()
        s.InitializeParkingLot(4)
        s.lotHandler.GetSlotNumsByColor = MagicMock(return_value = ['2', '4'])
        status = s.SlotNumsByColor('Red')
        self.assertEqual(status, '2, 4')
    
    def test_slot_fro_reg_num(self):
        s = EntryService()
        s.InitializeParkingLot(4)
        s.lotHandler.GetSlotNumByRegNum = MagicMock(return_value = '2')
        status = s.SlotNumForRegNum('KA-01-HH-9999')
        self.assertEqual(status, '2')

    def test_check_car_already_parked(self):
        s = EntryService()
        s.InitializeParkingLot(4)
        s.lotHandler.IsCarParked = MagicMock(return_value = True)

        result = s.CheckCarParkedAlready(Car('KA-01-HH-1234','White'))
        self.assertTrue(result)
        
