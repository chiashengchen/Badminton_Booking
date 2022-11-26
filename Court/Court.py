
class Court :
    def __init__(self, time, num, xpath):
        self._time = time
        self._num = num
        self._xpath = xpath

    def getTime(self):
        return self._time

    def getNum(self):
        return self._num
        
    def getXPath(self):
        return self._xpath