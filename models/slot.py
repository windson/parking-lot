class Slot(object):
    
    def __init__(self, _slotNum):
        self.slotNum = _slotNum
        self.isAvailable = True
        self.parkedCar = None
    
    @property
    def SlotNum(self):
        return self.slotNum
    
    @property
    def IsAvailable(self):
        return self.isAvailable
    
    @property
    def ParkedCar(self):
        return self.parkedCar
    
    @ParkedCar.setter
    def ParkedCar(self, value):
        if value == None:
            self.isAvailable = True
        else:
            self.isAvailable = False
        self.parkedCar = value
