import threading
from selenium import webdriver
from jsonschema import SchemaError
from Time.ScheduledTime import ScheduledTime
from Info.PersonalInfo import PersonalInfo
from SportsCenterState.State import State
class SportsCenter(threading.Thread):
    time : ScheduledTime
    info : PersonalInfo
    # driver : webdriver
    totalCourts : int
    state : State
    # emptyCourts : array
    targetTime : int
    orderNum : int

    def __init__(self, time, info):
        threading.Thread.__init__(self)
        self.time = time
        self.info = info
        self.targetTime = -1
        self.orderNum = 0
        self.emptyCourts = None

    def setState(self, state) :
        self.state = state

    def handle(self):
        self.state.handle(self)

    # thread start function
    def run(self):
        raise NotImplementedError("Not implement method yet !")

    def fakeRun(self):
        raise NotImplementedError("Not implement method yet !")
        
