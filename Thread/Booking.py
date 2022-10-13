from SportsCenterState.State import State
import threading
from Info.PersonalInfo import PersonalInfo
from Time.ScheduledTime import ScheduledTime
from selenium import webdriver
from Center.SportsCenter import SportsCenter
class Booking(threading.Thread) :
    state : State
    info : PersonalInfo
    time : ScheduledTime
    center : SportsCenter

    def __init__(self, time, info, center, state) :
        threading.Thread.__init__(self)
        self.time = time
        self.info = info
        self.state = state
        self.center = center
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get(center.url)

    def handle(self):
        self.state.handle(self)

    def setState(self, state):
        self.state = state

    def run(self):
        self.handle()

    def getScheduledTime(self):
        return self.time
    
    def getPersonalInfo(self):
        return self.info