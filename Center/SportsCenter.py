import threading
from Time.ScheduledTime import ScheduledTime
from Info.PersonalInfo import PersonalInfo
from SportsCenterState.State import State
class SportsCenter:
    time : ScheduledTime
    info : PersonalInfo
    totalCourts : int
    state : State
    targetTime : int
    orderNum : int
    appiontmentInterval : int

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
