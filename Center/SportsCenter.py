import threading
from Time.ScheduledTime import ScheduledTime
from Info.PersonalInfo import PersonalInfo
from datetime import datetime
class SportsCenter:
    url : str
    appointmentInterval : int
    totalCourt : int

    def __init__(self, url, totalCourt):
        self.url = url
        self.totalCourt = totalCourt

    # thread start function
    def run(self):
        raise NotImplementedError("Not implement method yet !")

    def fakeRun(self):
        raise NotImplementedError("Not implement method yet !")
        
