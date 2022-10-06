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