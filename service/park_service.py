from abc import ABC, abstractmethod
from service.lot_handler import LotHandler

class ParkService(ABC):

    def initialize_lot(self):
        pass

    def validate_car_in_slot(self, car):
        pass

    def allow(self, car):
        pass

class EntryService(ParkService):
    def allow(self, car):
        pass

class ExitService(ParkService):

    def allow(self, car):
        pass