from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from Center.SportsCenter import SportCenter
from Time.ScheduledTime import DayPeriods, ScheduledTime
from Info.PersonalInfo import PersonalInfo

class YongheSportCenter(SportCenter):
    def __init__(self, time, info):
        SportCenter.__init__(self, time, info)
        self.court = 6
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://scr.cyc.org.tw/tp10.aspx?module=login_page&files=login&PT=1')
        self.alert = Alert(self.driver)
    
    def findEmptyCourt(self, startTime, endTime) :
        emptyCourts = []
        for time in range(startTime, endTime):
            courts = []
            for i in range(self.court) :
            # 2 + startTime * self.court
                if i == 0:
                    td = 4
                else :
                    td = 3
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
        verification_code = input()
        password = self.driver.find_element(By.XPATH, '//*[@id=\"ContentPlaceHolder1_Captcha_text\"]') #網頁的密碼點
        password.clear()
        password.send_keys(verification_code)
        self.driver.find_element(By.XPATH, '//*[@id=\"login_but\"]').click()
        self.driver.find_element(By.XPATH, '//*[@title=\"羽球\"]').click()
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
            raise BaseException("Not enough courts !!" + str(len(emptyCourts)))
        for time in range(self.scheduledTime.hours):
            print(time)
        self.driver.find_element(By.XPATH, '//tbody/tr[8]/td[4]/img[1]').click()
        print(self.alert.text)
        # 已被預約！
        self.alert.accept() 
        # driver.find_element(By.XPATH, '//*[@onclick="if(confirm(\'您是否確定預約「羽\d 06:00~07:00」？\')){Step3Action(1137,6)}"').click()

        # <img name="PlaceBtn" src="img/sche01.png" width="87" height="21" onclick="if(confirm('您是否確定預約「羽5 06:00~07:00」？')){Step3Action(1137,6)}">
        print('finish')

if __name__ == '__main__':
    year = 2022
    month = input()
    day = input()
    time = ScheduledTime(year, month, day, 0, 0)
    personalInfo = PersonalInfo('A000000000', '123456')
    center = YongheSportCenter(time, personalInfo)
    center.fakeRun()