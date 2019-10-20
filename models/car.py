class Car(object):

    def __init__(self, _regNum, _color):
        self.regNum = _regNum
        self.color = _color

    @property
    def RegNum(self):
        return self.regNum
    
    @property
    def Color(self):
        return self.color
