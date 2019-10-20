import sys, os
from service.park_service import EntryService, ExitService
from models.car import Car
from util.constants import *

class ProcessInput(object):

    def __init__(self):
        self.entrysvc = EntryService()
        self.exsvc = ExitService()
        self.serviceInstance = None
        self.valid_actions = ['create_parking_lot',
            'park', 
            'leave', 
            'status', 
            'registration_numbers_for_cars_with_colour',
            'slot_numbers_for_cars_with_colour', 
            'slot_number_for_registration_number']    

    def interactive_mode(self):
        try:
            while True:
                inp = input()
                if inp.lower() == 'exit':
                    break
                else:
                    result = self.process(inp)
                    print(result)
        except (KeyboardInterrupt, SystemExit):
            return
        except Exception as ex:
            raise ex
        
    def file_input_mode(self, input_file):
        if not os.path.exists(input_file):
            raise FileNotFoundError('File {} does not exists'.format(input_file))

        with open(input_file, 'r') as fp:
            lines = fp.readlines()
            lines = [line.rstrip('\n') for line in lines]
            for inp in lines:
                res = self.process(inp)
                print(res)
            

    def process(self, inp):
        try:
            result = None
            cmds = inp.split()
            cmdlen = len(cmds)
            
            if cmdlen == 0:
                raise ValueError(UnknownErrorOccured)
                
            action = cmds[0]

            if action not in self.valid_actions:
                return TryAgain
                

            if action != 'create_parking_lot' and not self.entrysvc.IsInitialized:
                return MustCreateParkingLot

            if action == 'create_parking_lot':
                if cmdlen != 2:
                    return action + ' Error. ' + TryAgain

                capacity = int(cmds[1])
                
                result, self.serviceInstance = self.entrysvc.InitializeParkingLot(capacity)
                return result

            elif action == 'park':
                if cmdlen != 3:
                    return action + ' Error. ' + TryAgain
                
                regNum = cmds[1]
                color = cmds[2]
                car = Car(regNum,color)
                result = self.entrysvc.allow(car)

            elif action == 'leave': 
                if cmdlen != 2:
                    return action + ' Error. ' + TryAgain
                
                slotNum = cmds[1]
                self.exsvc.lotHandler = self.serviceInstance
                result = self.exsvc.allow(slotNum)
                
            elif action == 'status': 
                if cmdlen != 1:
                    return action + ' Error. ' + TryAgain

                slots = self.entrysvc.ShowStatus()
                status = 'Slot No.{0}Registration No{0}Colour{0}\n'.format('\t')
                for slot in slots:
                    if slot.ParkedCar is not None:
                        status += '{}\t{}\t{}\n'.format(slot.SlotNum, slot.ParkedCar.RegNum, slot.ParkedCar.Color)
                result = status
                    
            elif action == 'registration_numbers_for_cars_with_colour':
                if cmdlen != 2:
                    return action + ' Error. ' + TryAgain
                    
                color = cmds[1]
                result = self.entrysvc.RegNumsByColor(color)

            elif action == 'slot_numbers_for_cars_with_colour':
                if cmdlen != 2:
                    return action + ' Error. ' + TryAgain

                color = cmds[1]
                result = self.entrysvc.SlotNumsByColor(color)

            elif action == 'slot_number_for_registration_number':
                if cmdlen != 2:
                    return action + ' Error. ' + TryAgain

                regNum = cmds[1]
                result = self.entrysvc.SlotNumForRegNum(regNum)

            else:
                return InvalidAction
            
            return result

        except Exception as ex:
            raise ex
