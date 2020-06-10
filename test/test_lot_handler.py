import unittest
from service.lot_handler import LotHandler
from models.slot import Slot
from models.car import Car

class test_lot_handler(unittest.TestCase):
    
    def test_lot_handler_initalize(self):
        lh = LotHandler(6)
        self.assertEqual(lh.capacity, 6)
        self.assertEqual(len(lh.slots), 6)
        self.assertEqual(len(lh.freeSlots), 6)
        for i in range(0,6):
            self.assertTrue(lh.slots[i].IsAvailable)

    def test_fill_slot_invalid_slot_num(self):
        # Arrange
        lh = LotHandler(2)
        firstCar = Car('KA-01-HH-1234', 'White')

        # Act
        with self.assertRaises(ValueError) as ex:
            lh.FillSlot(firstCar, 3)
        
        # Assert 
        self.assertEqual('No Such Slot Number foudn in Parking Lot', str(ex.exception))
        
        
    def test_fill_slot(self):
        # Arrange
        lh = LotHandler(2)
        firstCar = Car('KA-01-HH-1234', 'White')
        secondCar = Car('KA-01-HH-1231', 'Red')

        # Act
        filledSlot1 = lh.FillSlot(firstCar, 1)
        

        # Assert firstCar
        self.assertEqual(filledSlot1.SlotNum,1)
        self.assertFalse(filledSlot1.IsAvailable)
        self.assertEqual(filledSlot1.ParkedCar,firstCar)
        self.assertFalse(lh.IsLotFull())

        
        # Act secondCar
        
        filledSlot2 = lh.FillSlot(secondCar, 2)
        # Assert secondCar
        self.assertEqual(filledSlot2.SlotNum,2)
        self.assertFalse(filledSlot2.IsAvailable)
        self.assertEqual(filledSlot2.ParkedCar,secondCar)


        self.assertTrue(lh.IsLotFull())
    
    def test_car_parked_already(self):
        # Arrange
        lh = LotHandler(2)
        firstCar = Car('KA-01-HH-1234', 'White')
        duplicateCar = Car('KA-01-HH-1234', 'White')

        # Act
        lh.FillSlot(firstCar, 1)
        lh.FillSlot(duplicateCar, 2)

        # Assert
        self.assertTrue(lh.IsCarParked(duplicateCar))

    def test_vaccate_slot(self):
        # Arrange
        lh = LotHandler(2)
        firstCar = Car('KA-01-HH-1234', 'White')
        secondCar = Car('KA-01-BB-0001', 'Red')
        
        lh.FillSlot(firstCar, 1)
        lh.FillSlot(secondCar, 2)

        slotNumToVaccate = 1
        lh.VaccateSlot(slotNumToVaccate)
        self.assertTrue(slotNumToVaccate in lh.freeSlots)
        self.assertTrue(2 not in lh.freeSlots)
    
    def test_vaccate_slot_not_present(self):
        # Arrange
        lh = LotHandler(2)
        firstCar = Car('KA-01-HH-1234', 'White')
        secondCar = Car('KA-01-BB-0001', 'Red')
        
        lh.FillSlot(firstCar, 1)
        lh.FillSlot(secondCar, 2)

        slotNumToVaccate = 3
        with self.assertRaises(ValueError) as ex:
            lh.VaccateSlot(slotNumToVaccate)
        self.assertEqual(ex.exception, 'No such Slot Number found in Parking lots')
    
    def test_is_slot_available(self):
        # Arrange
        lh = LotHandler(2)
        firstCar = Car('KA-01-HH-1234', 'White')
        

        # Act
        filledSlot = lh.FillSlot(firstCar, 1)
        
        # Assert
        self.assertFalse(lh.IsSlotAvailable(filledSlot.SlotNum))
        self.assertTrue(lh.IsSlotAvailable(2))

    def test_get_slot_nums_by_color(self):
        # Arrange
        lh = LotHandler(4)
        car1 = Car('KA-01-HH-1234', 'White')
        car2 = Car('KA-04-HH-1231', 'Blue')
        car3 = Car('KA-08-HH-1111', 'Red')
        car4 = Car('KA-02-HH-9999', 'Blue')

        lh.FillSlot(car1, 1)
        lh.FillSlot(car2, 2)
        lh.FillSlot(car3, 3)
        lh.FillSlot(car4, 4)

        expectedBlueSlots = ['2','4']
        expectedRedslots = ['3']
        

        # Act
        actualBlueSlots = lh.GetSlotNumsByColor('Blue')
        actualRedSlots =  lh.GetSlotNumsByColor('Red')
        actualYellowSlots = lh.GetSlotNumsByColor('Yellow')
        # Assert
        self.assertEqual(expectedBlueSlots,actualBlueSlots)
        self.assertEqual(expectedRedslots,actualRedSlots)
        self.assertEqual([],actualYellowSlots)

    def test_get_slot_num_by_reg_num(self):
        # Arrange
        lh = LotHandler(4)
        car1 = Car('KA-01-HH-1234', 'White')
        car2 = Car('KA-04-HH-1231', 'Blue')
        car3 = Car('KA-08-HH-1111', 'Red')
        car4 = Car('KA-02-HH-9999', 'Blue')

        lh.FillSlot(car1, 1)
        lh.FillSlot(car2, 2)
        lh.FillSlot(car3, 3)
        lh.FillSlot(car4, 4)

        expectedSlotNum = '2'
        
        

        # Act
        actualSlotNum = lh.GetSlotNumByRegNum('KA-04-HH-1231')
        actualNotFound =  lh.GetSlotNumByRegNum('KA-04-HH-3333')
        
        # Assert
        self.assertEqual(expectedSlotNum,actualSlotNum)
        self.assertEqual('Not Found',actualNotFound)


    def test_get_reg_nums_by_color(self):
        # Arrange
        lh = LotHandler(4)
        car1 = Car('KA-01-HH-1234', 'White')
        car2 = Car('KA-04-HH-1231', 'Blue')
        car3 = Car('KA-04-HH-1231', 'Red')
        car4 = Car('KA-04-HH-1231', 'Blue')

        lh.FillSlot(car1, 1)
        lh.FillSlot(car2, 2)
        lh.FillSlot(car3, 3)
        lh.FillSlot(car4, 4)

        expectedBlueRegNums = ['KA-04-HH-1231', 'KA-04-HH-1231']
        expectedRedRegNums = ['KA-04-HH-1231']
        

        # Act
        actualBlueRegNums = lh.GetRegNumsByColor('Blue')
        actualRedRegNums =  lh.GetRegNumsByColor('Red')
        actualYellowRegNums = lh.GetRegNumsByColor('Yellow')
        # Assert
        self.assertEqual(expectedBlueRegNums,actualBlueRegNums)
        self.assertEqual(expectedRedRegNums,actualRedRegNums)
        self.assertEqual([],actualYellowRegNums)


    def test_get_nearest_slot(self):
        # Arrange
        lh = LotHandler(4)
        car1 = Car('KA-01-HH-1234', 'White')
        car2 = Car('KA-04-HH-1231', 'Blue')
        car3 = Car('KA-04-HH-1231', 'Red')
        car4 = Car('KA-04-HH-1231', 'Blue')

        lh.FillSlot(car1, 1)
        lh.FillSlot(car2, 2)
        lh.FillSlot(car3, 3)
        lh.FillSlot(car4, 4)

        lh.VaccateSlot(2)
        lh.VaccateSlot(4)

        # Act
        val = lh.GetNearestSlot()
        # Assert
        self.assertEqual(val,2)