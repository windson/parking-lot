import unittest
from unittest import mock
from util.constants import *
from input_processor import ProcessInput
from models.slot import Slot
from models.car import Car

class test_input_processor(unittest.TestCase):
    
    def test_process_input_unkonw_error(self):
        # Arrange
        s = ProcessInput()
        inp =''
        
        # Act 
        with self.assertRaises(ValueError) as ex:
            s.process('')

        # Assert
        self.assertEqual(UnknownErrorOccured, str(ex.exception))
        
    
    def test_process_input_leave_first(self):
        # Arrange
        s = ProcessInput()
        inp ='leave 4'
        
        # Act 
        res = s.process(inp)

        # Assert
        self.assertEqual(MustCreateParkingLot, res)
        
    def test_process_input_create_parking_lot(self):
        # Arrange
        s = ProcessInput()
        slots = 2
        inp ='create_parking_lot {}'.format(slots)
        
        # Act 
        res = s.process(inp)

        # Assert
        self.assertEqual(ParkingLotInit.format(slots), res)

    
    def test_process_input_create_parking_lot_invalid_args_(self):
        # Arrange
        s = ProcessInput()
        slots = 2

        # Act 
        inp ='create_parking_lot {} test'.format(slots)
        res = s.process(inp)

        # Assert
        self.assertEqual('create_parking_lot Error. ' + TryAgain, res)


    def test_process_input_park(self):
        # Arrange
        s = ProcessInput()
        slots = 2
        inp ='create_parking_lot {}'.format(slots)
        res = s.process(inp)
        # Act 
        inp ='park KA-01-HH-1234 White'
        res = s.process(inp)

        # Assert
        self.assertEqual(Parked.format(1), res)
    

    def test_process_input_park_invalid_arg(self):
        # Arrange
        s = ProcessInput()
        slots = 2
        inp ='create_parking_lot {}'.format(slots)
        res = s.process(inp)
        # Act 
        inp ='park KA-01-HH-1234 White sdf'
        res = s.process(inp)

        # Assert
        self.assertEqual('park Error. ' + TryAgain, res)



    def test_process_input_leave(self):
        # Arrange
        s = ProcessInput()
        slots = 2

        inp ='create_parking_lot {}'.format(slots)
        res = s.process(inp)

        inp ='park KA-01-HH-1234 White'
        res = s.process(inp)

        # Act 
        inp = 'leave 1'
        res =s.process(inp)

        # Assert
        self.assertEqual(SlotFreed.format(1), res)
    

    def test_process_input_leave_invalid_args(self):
        # Arrange
        s = ProcessInput()
        slots = 2

        inp ='create_parking_lot {}'.format(slots)
        res = s.process(inp)

        inp ='park KA-01-HH-1234 White'
        res = s.process(inp)

        # Act 
        inp = 'leave'
        res =s.process(inp)

        # Assert
        self.assertEqual('leave Error. ' + TryAgain, res)


    def test_process_input_status(self):
        # Arrange
        s = ProcessInput()
        slots = 2

        inp ='create_parking_lot {}'.format(slots)
        res = s.process(inp)

        inp ='park KA-01-HH-1234 White'
        res = s.process(inp)

        inp ='park KA-01-HH-1111 Red'
        res = s.process(inp)

        # Act 
        inp = 'status'
        res =s.process(inp)

        # Assert
        self.assertTrue('KA-01-HH-1111' in res)
        self.assertTrue('KA-01-HH-1234' in res)
    
    
    def test_process_input_status_invalid_args(self):
        # Arrange
        s = ProcessInput()
        slots = 2

        inp ='create_parking_lot {}'.format(slots)
        res = s.process(inp)

        inp ='park KA-01-HH-1234 White'
        res = s.process(inp)

        inp ='park KA-01-HH-1111 Red'
        res = s.process(inp)

        # Act 
        inp = 'status blah'
        res =s.process(inp)

        # Assert
        self.assertEqual('status Error. ' + TryAgain, res)
    
    
    def test_process_input_registration_numbers_for_cars_with_colour(self):
        # Arrange
        s = ProcessInput()
        slots = 4

        inp ='create_parking_lot {}'.format(slots)
        s.process(inp)

        inp ='park KA-01-HH-1234 White'
        s.process(inp)

        inp ='park KA-01-HH-9999 Red'
        s.process(inp)
        inp ='park KA-01-HH-1114 Blue'
        s.process(inp)
        inp ='park KA-01-HH-1145 Red'
        s.process(inp)

        # Act 
        inp = 'registration_numbers_for_cars_with_colour Red'
        res = s.process(inp)

        # Assert
        self.assertEqual('KA-01-HH-9999, KA-01-HH-1145', res)
        

    def test_process_input_registration_numbers_for_cars_with_colour_invalid_args(self):
        # Arrange
        s = ProcessInput()
        slots = 4

        inp ='create_parking_lot {}'.format(slots)
        s.process(inp)

        inp ='park KA-01-HH-1234 White'
        s.process(inp)

        inp ='park KA-01-HH-9999 Red'
        s.process(inp)
        inp ='park KA-01-HH-1114 Blue'
        s.process(inp)
        inp ='park KA-01-HH-1145 Red'
        s.process(inp)

        # Act 
        inp = 'registration_numbers_for_cars_with_colour Red blah'
        res = s.process(inp)

        # Assert
        self.assertEqual('registration_numbers_for_cars_with_colour Error. ' + TryAgain, res)
        
    
    def test_process_input_slot_numbers_for_cars_with_colour(self):
        # Arrange
        s = ProcessInput()
        slots = 4

        inp ='create_parking_lot {}'.format(slots)
        s.process(inp)

        inp ='park KA-01-HH-1234 White'
        s.process(inp)

        inp ='park KA-01-HH-9999 Red'
        s.process(inp)
        inp ='park KA-01-HH-1114 Blue'
        s.process(inp)
        inp ='park KA-01-HH-1145 Red'
        s.process(inp)

        # Act 
        inp = 'slot_numbers_for_cars_with_colour Red'
        res = s.process(inp)

        # Assert
        self.assertEqual('2, 4', res)
        

    def test_process_input_slot_numbers_for_cars_with_colour_invalid_args(self):
        # Arrange
        s = ProcessInput()
        slots = 4

        inp ='create_parking_lot {}'.format(slots)
        s.process(inp)

        inp ='park KA-01-HH-1234 White'
        s.process(inp)

        inp ='park KA-01-HH-9999 Red'
        s.process(inp)
        inp ='park KA-01-HH-1114 Blue'
        s.process(inp)
        inp ='park KA-01-HH-1145 Red'
        s.process(inp)

        # Act 
        inp = 'slot_numbers_for_cars_with_colour Red blan'
        res = s.process(inp)

        # Assert
        self.assertEqual('slot_numbers_for_cars_with_colour Error. ' + TryAgain, res)

    
    def test_process_input_slot_number_for_registration_number(self):
        # Arrange
        s = ProcessInput()
        slots = 4

        inp ='create_parking_lot {}'.format(slots)
        s.process(inp)

        inp ='park KA-01-HH-1234 White'
        s.process(inp)

        inp ='park KA-01-HH-9999 Red'
        s.process(inp)
        inp ='park KA-01-HH-1114 Blue'
        s.process(inp)
        inp ='park KA-01-HH-1145 Red'
        s.process(inp)

        inp ='leave 3'
        s.process(inp)
        inp ='leave 1'
        s.process(inp)

        inp ='park KA-01-BB-8877 Red'
        s.process(inp)

        # Act 
        inp = 'slot_number_for_registration_number KA-01-BB-8877'
        res = s.process(inp)

        # Assert
        self.assertEqual('1', res)
            

    def test_process_input_slot_number_for_registration_number_not_found(self):
        # Arrange
        s = ProcessInput()
        slots = 4

        inp ='create_parking_lot {}'.format(slots)
        s.process(inp)

        inp ='park KA-01-HH-1234 White'
        s.process(inp)

        inp ='park KA-01-HH-9999 Red'
        s.process(inp)
        inp ='park KA-01-HH-1114 Blue'
        s.process(inp)
        inp ='park KA-01-HH-1145 Red'
        s.process(inp)

        inp ='leave 3'
        s.process(inp)
        inp ='leave 1'
        s.process(inp)

        inp ='park KA-01-BB-8877 Red'
        s.process(inp)

        # Act 
        inp = 'slot_number_for_registration_number TS-01-BB-8877'
        res = s.process(inp)

        # Assert
        self.assertEqual('Not Found', res)
            

    
    def test_process_input_slot_number_for_registration_number_invalid_args(self):
        # Arrange
        s = ProcessInput()
        slots = 4

        inp ='create_parking_lot {}'.format(slots)
        s.process(inp)

        inp ='park KA-01-HH-1234 White'
        s.process(inp)

        inp ='park KA-01-HH-9999 Red'
        s.process(inp)
        inp ='park KA-01-HH-1114 Blue'
        s.process(inp)
        inp ='park KA-01-HH-1145 Red'
        s.process(inp)

        inp ='leave 3'
        s.process(inp)
        inp ='leave 1'
        s.process(inp)

        inp ='park KA-01-BB-8877 Red'
        s.process(inp)

        # Act 
        inp = 'slot_number_for_registration_number KA-01-BB-8877 blah'
        res = s.process(inp)

        # Assert
        self.assertEqual('slot_number_for_registration_number Error. ' + TryAgain, res)
            

    def test_process_input_exhausted_leaves(self):
        # Arrange
        s = ProcessInput()
        slots = 2

        inp ='create_parking_lot {}'.format(slots)
        s.process(inp)

        inp ='park KA-01-HH-1234 White'
        s.process(inp)

        inp ='park KA-01-HH-9999 Red'
        s.process(inp)

        inp ='leave 2'
        s.process(inp)
        inp ='leave 1'
        s.process(inp)

        # Act 
        inp ='leave 1'
        res = s.process(inp)

        # Assert
        self.assertEqual('Slot number 1 is free', res)
            
    def test_process_input_sorry_parking_slot_full(self):
        # Arrange
        s = ProcessInput()
        slots = 2

        inp ='create_parking_lot {}'.format(slots)
        s.process(inp)

        inp ='park KA-01-HH-1234 White'
        s.process(inp)

        inp ='park KA-01-HH-9999 Red'
        s.process(inp)

        # Act 
        
        inp ='park KA-01-HH-0000 Red'
        res = s.process(inp)

        # Assert
        self.assertEqual('Sorry, parking lot is full', res)
            

# create_parking_lot 6
# park KA-01-HH-1234 White
# park KA-01-HH-9999 White
# park KA-01-BB-0001 Black
# park KA-01-HH-7777 Red
# park KA-01-HH-2701 Blue
# park KA-01-HH-3141 Black
# leave 4
# status
# park KA-01-P-333 White
# park DL-12-AA-9999 White
# registration_numbers_for_cars_with_colour White
# slot_numbers_for_cars_with_colour White
# slot_number_for_registration_number KA-01-HH-3141
# slot_number_for_registration_number MH-04-AY-1111