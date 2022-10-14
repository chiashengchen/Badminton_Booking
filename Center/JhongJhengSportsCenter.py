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
        print(type(self.driver))
        self.driver.get('https://www.cjcf.com.tw/jj01.aspx?module=login_page&files=login&PT=1') 
        self.state = LoginState()
    
    def run(self):
        self.state.handle(self)

    def findEmptyCourt(self, startTime, endTime) :
        emptyCourts = []
        for time in range(startTime, endTime):
            courts = []
            for i in range(self.court) :
                td = 4
                if "alert" in self.driver.find_element(By.XPATH, '//tbody/tr[' + str(2 + time * self.court + i) + ']/td[' + str(td) + ']/img[1]').get_attribute("onclick"):
                    continue
                courts.append('//tbody/tr[' + str(2 + time * self.court + i) + ']/td[4]/img[1]')
            if len(courts) >= self.scheduledTime.court:
                emptyCourts.append(courts)
        return emptyCourts

    # TODO : try & except
    def fakeRun(self):
        startTime = 0
        endTime = 0
        brookingDay = self.scheduledTime.getScheduledDate()
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = self.driver.current_window_handle
        try:
            self.driver.find_element(By.XPATH, u'//a[text()="確定"]').click()
        except UnexpectedAlertPresentException:
            print('UnexpectedAlertPresentException')
        try:
            self.driver.find_element(By.XPATH, u'//a[text()="確定"]').click()
        except UnexpectedAlertPresentException:
            print('UnexpectedAlertPresentException')
        
        # Login
        account = self.driver.find_element(By.XPATH, "//*[@id=\"ContentPlaceHolder1_loginid\"]")
        account.clear()
        # 身分證
        account.send_keys(self.personalInfo.getAccount())
        password = self.driver.find_element(By.XPATH, '//*[@id=\"loginpw\"]') #網頁的密碼點
        password.clear()
        # 密碼
        password.send_keys(self.personalInfo.getPassword())
        
        WebDriverWait(self.driver, 10).until(lambda driver: len(self.driver.find_element(By.XPATH, '//*[@id=\"ContentPlaceHolder1_Captcha_text\"]').get_attribute("value")) == 5)
        self.driver.find_element(By.XPATH, '//*[@id=\"login_but\"]').click()
        self.driver.find_element(By.XPATH, '//*[@title=\"羽球\"]').click()
        self.alert.accept()
        self.driver.find_element(By.XPATH, '//*[@src=\"img/conf01.png\"]').click()
        self.alert.accept()
        self.driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + brookingDay+ '\',1)\"]').click()

        if self.scheduledTime.getCalendarDayPeriods() == DayPeriods.AFTERNOON:
            self.driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[2]').click()
            startTime = self.scheduledTime.startTime - 12
            endTime = self.scheduledTime.endTime - 12
            
        elif self.scheduledTime.getCalendarDayPeriods() == DayPeriods.EVENING:
            self.driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[3]').click()
            startTime = self.scheduledTime.startTime - 18
            endTime = self.scheduledTime.endTime - 18

        else :
            startTime = self.scheduledTime.startTime - 6
            endTime = self.scheduledTime.endTime - 6
        
        emptyCourts = self.findEmptyCourt(startTime, endTime)
        if len(emptyCourts) < self.scheduledTime.hours:
            print("Not enough courts !!")
            return
            # raise BaseException("Not enough courts !!" + str(len(emptyCourts)))

        for time in range(self.scheduledTime.hours):
            for court in range(self.scheduledTime.court):
                if(time != 0 or court != 0) : 
                    self.driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + brookingDay+ '\',1)\"]').click()
                self.driver.find_element(By.XPATH, emptyCourts[time][court]).click()
                self.alert.accept()
                # loading
                self.driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[3]').click()
        print('finish')
