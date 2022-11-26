import threading
import SportsCenterState.State as State
import Info.PersonalInfo as Info
import Center.SportsCenter as Center
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import Time.ScheduledTime as ScheduledTime
class Content(threading.Thread):
    driver : webdriver.Chrome
    def __init__(self, center : Center.SportsCenter, info : Info.PersonalInfo, state : State.State, time : ScheduledTime.ScheduledTime, lock):
        threading.Thread.__init__(self)
        self._center = center
        self._info = info
        self._state = state
        self._lock = lock
        self._time = time
        self._driver = self.initDriver(center.getURL())

    def initDriver(self, url):
        opts = Options()
        opts.add_argument("--incognito")  
        ua = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
        opts.add_argument("user-agent={}".format(ua))  
        driver = webdriver.Chrome(executable_path='./chromedriver',chrome_options=opts)
        try :
            driver.get(url)
        except :
            print("error: cannot load page")
        return driver

    def getDriver(self):
        return self._driver

    def handle(self):
        self._state.handle(self)

    def run(self):
        self._state.handle(self)

    def getCenter(self):
        return self._center
    
    def getInfo(self):
        return self._info
    
    def setState(self, state):
        self._state = state

    def getTime(self):
        return self._time
    
    def getLock(self):
        return self._lock