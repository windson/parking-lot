from models.slot import Slot
from models.car import Car

class LotHandler(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.freeSlots = []
        self.slots = []
        for i in range(0,capacity):
            slot = Slot(i+1)
            self.freeSlots.append(i+1)
            self.slots.append(slot)


    def FillSlot(self, car, slotNum):
        filledSlot = None
        for slot in self.slots:
            if slot.slotNum == slotNum:
                slot.ParkedCar = car
                self.freeSlots.remove(slotNum)
                filledSlot = slot                
        
        if filledSlot == None:
            raise ValueError('No Such Slot Number foudn in Parking Lot')
        else:
            return filledSlot
        
    
    def VaccateSlot(self, slotNum):

        for slot in self.slots:
            if slot.slotNum == slotNum:
                slot.ParkedCar = None
                self.freeSlots.append(slotNum)

    def GetNearestSlot(self):
        sNum = min(self.freeSlots)
        nearestSlot = [slot for slot in self.slots if slot.SlotNum == sNum][0]
        return nearestSlot

    def IsCarParked(self, car):
        status = False
        for slot in self.slots:
            if slot.IsAvailable == False: # Check only parked slots
                if slot.ParkedCar is not None:
                    status = slot.ParkedCar.RegNum == car.RegNum
        return status
        

    def IsLotFull(self):
        return len(self.freeSlots) == 0


    def IsSlotAvailable(self, slotNum):
        return slotNum in self.freeSlots

    
    def GetSlotNumsByColor(self, color):
        # slot_numbers_for_cars_with_colour
        slots = []
        for slot in self.slots:
            if slot.ParkedCar != None:
                if str(slot.ParkedCar.Color).lower() == color.lower():
                    slots.append(slot.SlotNum)
        
        return slots

    def GetSlotNumByRegNum(self, regNum):
        # slot_number_for_registration_number
        slotNum = 'Not Found'
        for slot in self.slots:
            if slot.ParkedCar != None:
                if str(slot.ParkedCar.RegNum).lower() == regNum.lower():
                    slotNum = str(slot.SlotNum)
                    break
        
        return slotNum

    def GetRegNumsByColor(self, color):
        # registration_numbers_for_cars_with_colour
        regNums = []
        for slot in self.slots:
            if slot.ParkedCar != None:
                if str(slot.ParkedCar.Color).lower() == color.lower():
                    regNums.append(str(slot.ParkedCar.RegNum))
        
        return regNums
        