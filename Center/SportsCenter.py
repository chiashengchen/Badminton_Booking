import datetime
from Time.ScheduledTime import ScheduledTime
from Info.PersonalInfo import PersonalInfo
from SportsCenterState.State import State
class SportsCenter:
    _time : ScheduledTime
    info : PersonalInfo
    _totalCourts : int
    state : State
    _targetTime : int
    _orderNum : int
    _appiontmentInterval : int

    def __init__(self, time):
        self._time = time
        self._targetTime = -1
        self._orderNum = 0
        self._targetCourts = []
        self._emptyCourts = []
        self._isCount = False

    def getTime(self):
        return self._time

    def setTargetTime(self, time):
        self._targetTime = time
    
    def setTargetCourts(self, courts):
        self._targetCourts = courts
    
    def getTargetCourts(self):
        return self._targetCourts
    
    def getEmptyCourts(self):
        return self._emptyCourts

    def setEmptyCourts(self, courts):
        self._emptyCourts = courts

    def getURL(self):
        return self._url
    
    def isCount(self):
        return self._isCount
    
    def setCount(self, bool):
        self._isCount = bool

    def isDateAvailable(self):
        now = datetime.datetime.now()
        appointment = self._time.getScheduledDate()
        # 假如 date 不能點，但其實是沒出現。給 30 秒的 buffer
        target = datetime.datetime.strptime(appointment, "%Y/%m/%d/%S")
        # target = datetime.datetime.strptime(appointment, "%Y/%m/%d")
        delta = target - now
        if(delta.days < 0 or delta.days >= (self._bookingGap - 1)):
            return 0
        else :
            return 1
        
    def isWithinSec(self, sec : int):
        now = datetime.datetime.now()
        appointment = self._time.getScheduledDate()
        target = datetime.datetime.strptime(appointment, "%Y/%m/%d/%S")
        delta = target - now
        print(str(delta.seconds) + " seconds left")
        if(delta.days == (self._bookingGap - 1) and delta.seconds < sec):
            return 1
        else :
            return 0

    def getName(self):
        return self._name