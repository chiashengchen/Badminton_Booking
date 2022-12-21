import datetime
from prometheus_client import Enum

class DayPeriods(Enum):
    MORNING = 0
    AFTERNOON = 1
    EVENING = 2

class ScheduledTime: 
    year : int
    month : int
    day : int
    startTime : int
    endTime : int 
    hours : int
    court : int
    
    def __init__(self, year, month, day, startTime, endTime, hours, court):
        self._year = int(year)
        self._month = int(month)
        self._day = int(day)
        self._startTime = int(startTime)
        self._endTime = int(endTime)
        self._hours = int(hours)
        self._court = int(court)
        self._bufferTime = 30
        if self._endTime <= self._startTime or self._startTime < 6 or self._endTime >= 23:
            raise BaseException("Time Invalid Error")
        if not self.isVaildDate():
            raise BaseException("Date Invalid Error")

    def getScheduledDate(self):
        if self._month < 10:
            brookingDay = str(self._year) + '/0'+ str(self._month)
        else:
            brookingDay = str(self._year) + '/'+ str(self._month)
        if self._day < 10:
            brookingDay = brookingDay + '/0' + str(self._day)
        else:
            brookingDay = brookingDay + '/' + str(self._day)
        brookingDay = brookingDay + '/' + str(self._bufferTime)
        return brookingDay

    def getCalendarDayPeriods(self):
        if self._startTime >= 18:
            return 2
        elif self._startTime >= 12:
            return 1
        else:
            return 0

    def getStartTime(self):
        return self._startTime

    def getEndTime(self):
        return self._endTime

    def getOrderCourts(self):
        return self._court
    
    def getOrderTime(self):
        return self._hours

    def isVaildDate(self):
        now = datetime.datetime.now()
        target = datetime.datetime.strptime(self.getScheduledDate(), "%Y/%m/%d/%S")
        delta = target - now
        if(delta.days < 0):
            return 0
        else :
            return 1