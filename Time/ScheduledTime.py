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
        self.year =int(year)
        self.month = int(month)
        self.day = int(day)
        self.startTime = int(startTime)
        self.endTime = int(endTime)
        self.hours = int(hours)
        self.court = int(court)
        if self.endTime <= self.startTime:
            raise BaseException("Error")

    def getScheduledDate(self):
        if self.day < 10:
            brookingDay = str(self.year) + '/'+ str(self.month) + '/0' + str(self.day)
        else:
            brookingDay = str(self.year) + '/'+ str(self.month) + '/' + str(self.day)
        return brookingDay

    def getCalendarDayPeriods(self):
        if self.startTime >= 18:
            return 2
        elif self.startTime >= 12:
            return 1
        else:
            return 0
