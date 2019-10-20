from abc import ABC, abstractmethod
from service.lot_handler import LotHandler

class ParkService(ABC):

    def __init__(self):
        self.lotHandler = None

    def InitializeParkingLot(self, capacity):
        if self.lotHandler is None:
            self.lotHandler = LotHandler(capacity)
        else:
            raise Exception('Already Initialized Parking Lot')

    def CheckCarParkedAlready(self, car):
        return self.lotHandler.IsCarParked(car)
    
    @abstractmethod
    def allow(self, car):
        pass
        

class EntryService(ParkService):
    
    def allow(self, car, slotNum):
        
        # First Check lot is full
        if self.lotHandler.IsLotFull() == True:
            return 'Sorry, parking lot is full'
        
        # Check car already parked: Invalid input
        if self.lotHandler.IsCarParked(car) == True:
            ValueError('Cannot park already Parked Car: {0}'.format(car.RegNum))

        # Check slot available
        if self.lotHandler.IsSlotAvailable(slotNum) == True:
            pass



class ExitService(ParkService):

    def InitializeParkingLot(self, capacity):
        raise AttributeError('ExitService Cannot create Parking Lot')
    
    def allow(self, car):
        pass