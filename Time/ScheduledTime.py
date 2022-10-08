class ScheduledTime: 
    year : int
    month : int
    day : int
    startTime : int
    endTime : int 
    
    def __init__(self, year, month, day, startTime, endTime):
        self.year = year
        self.month = month
        self.day = day
        self.startTime = startTime
        self.endTime = endTime

    def getScheduledDate(self):
        if len(self.day) < 2:
            brookingDay = str(self.year) + '/'+ str(self.month) + '/0' + str(self.day)
        else:
            brookingDay = str(self.year) + '/'+ str(self.month) + '/' + str(self.day)
        return brookingDay