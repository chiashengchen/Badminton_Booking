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
        self._bookingGap = 3
        self._prepareTime  = 10
        self._bufferTime = 10
        if self._endTime <= self._startTime or self._startTime < 6 or self._endTime > 22:
            raise BaseException("Time Invalid Error")
        if not self.isVaildDate():
            raise BaseException("Date Invalid Error")

    def getScheduledDate(self):
        if self._month < 10:
            orderDay = str(self._year) + '/0'+ str(self._month)
        else:
            orderDay = str(self._year) + '/'+ str(self._month)
        if self._day < 10:
            orderDay = orderDay + '/0' + str(self._day)
        else:
            orderDay = orderDay + '/' + str(self._day)
        return orderDay

    def getScheduledDateWithBuffer(self):
        orderDay = self.getScheduledDate()
        orderDay = orderDay + '/' + str(self._bufferTime)
        return orderDay

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
        target = datetime.datetime.strptime(self.getScheduledDate(), "%Y/%m/%d")
        delta = target - now
        if(delta.days < 0):
            return 0
        else :
            return 1
    

    def isAfterPrepareTime(self):
        now = datetime.datetime.now()
        target = datetime.datetime.strptime(self.getScheduledDate(), "%Y/%m/%d")
        shift = datetime.timedelta(days=self._bookingGap)
        prepareTime = datetime.timedelta(seconds=self._prepareTime)
        now = now + shift
        target = target - prepareTime
        delta = target - now
        
        print("delta.day = {}", delta.days)
        print("delta.second = {}", delta.seconds)
        if delta.days > 0:
            return 1
        else :
            return 0

    def isAfterBufferTime(self):
        now = datetime.datetime.now()
        target = datetime.datetime.strptime(self.getScheduledDate(), "%Y/%m/%d")
        shift = datetime.timedelta(days=self._bookingGap)
        bufferTime = datetime.timedelta(seconds=self._bufferTime)
        now = now + shift
        target = target + bufferTime
        delta = target - now
        print("delta.day = {}", delta.days)
        print("delta.second = {}", delta.seconds)

if __name__ == '__main__':
    year = 2022
    month = 12
    day = 30
    startTime = 19
    endTime = 22
    hours = 2
    court = 1
    time2week = ScheduledTime(year, month, day, startTime, endTime, hours, court)
    print (time2week.isAfterPrepareTime())
    pass