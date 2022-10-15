from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from SportsCenterState.JhongJhengState.LoginState import LoginState
from Center.SportsCenter import SportsCenter
from Time.ScheduledTime import DayPeriods, ScheduledTime
from Info.PersonalInfo import PersonalInfo

class JhongJhengSportCenter(SportsCenter):
    def __init__(self, time, info):
        SportsCenter.__init__(self, time, info)
        self.totalCourts = 5
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.cjcf.com.tw/jj01.aspx?module=login_page&files=login&PT=1') 
        self.state = LoginState()
    
    def run(self):
        self.state.handle(self)
