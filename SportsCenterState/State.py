 
from Time.ScheduledTime import ScheduledTime
from Info.PersonalInfo import PersonalInfo
# from Thread.Booking import Booking # circular import ??

class State :
    scheduledTime : ScheduledTime
    personalInfo : PersonalInfo
    url : str
    appointmentInterval : int
    court : int
    # booking : Booking

    def __init__(self, time, info):
        self.scheduledTime = time
        self.personalInfo  = info
        
    def handle(self, booking):
        raise NotImplementedError("Not implement method yet !")