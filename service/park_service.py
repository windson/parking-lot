from abc import ABC, abstractmethod
from service.lot_handler import LotHandler
from util.constants import *

class ParkService(ABC):

    def __init__(self):
        self.lotHandler = None

    def InitializeParkingLot(self, capacity):
        if self.lotHandler is None:
            self.lotHandler = LotHandler(capacity)
            return ParkingLotInit.format(capacity)
        else:
            raise Exception('Already Initialized Parking Lot')

    def CheckCarParkedAlready(self, car):
        return self.lotHandler.IsCarParked(car)
    
    @abstractmethod
    def allow(self, car, slotNum):
        pass
        

class EntryService(ParkService):
    
    def allow(self, car):
        # Allow entry of the car in parking lot
        try:
            
            if car == None:
                raise ValueError(InvalidInput)

            # First Check lot is full
            if self.lotHandler.IsLotFull() == True:
                return ParkingLotFull
            
            # Check car already parked: Invalid input
            if self.lotHandler.IsCarParked(car) == True:
                raise ValueError(ReparkNotAllowed.format(car.RegNum))

            # Get nearest slot
            nearestSlotNum = self.lotHandler.GetNearestSlot()

            # check if slot available
            if self.lotHandler.IsSlotAvailable(nearestSlotNum) == False:
                raise ValueError(SlotUnAvailable)

            #park car in the slot
            filledSlot = self.lotHandler.FillSlot(car, nearestSlotNum)
            return Parked.format(filledSlot.SlotNum)
        except ValueError as ve:
            raise ve

        except:
            raise Exception(UnknownErrorOccured)




class ExitService(ParkService):

    def InitializeParkingLot(self, capacity):
        raise AttributeError(ExitServiceCantInit)
    
    def allow(self, slotNum):
        # Allow exit of the car from parking lot
        pass