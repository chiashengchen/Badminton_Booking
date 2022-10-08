import threading
from Time.ScheduledTime import ScheduledTime
from Info.PersonalInfo import PersonalInfo
from datetime import datetime
class SportCenter(threading.Thread):
    scheduledTime : ScheduledTime
    personalInfo : PersonalInfo
    url : str
    appointmentInterval : int

    def __init__(self, time, info):
        threading.Thread.__init__(self)
        self.scheduledTime = time
        self.personalInfo  = info

    # thread start function
    def run(self):
        raise NotImplementedError("Not implement method yet !")

    def fakeRun(self):
        raise NotImplementedError("Not implement method yet !")
        
