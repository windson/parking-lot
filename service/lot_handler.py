from models.slot import Slot
from models.car import Car

class LotHandler(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = []
        for i in range(0,capacity):
            slot = Slot(i+1)
            self.slots.append(slot)


        
    