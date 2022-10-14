from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from Center.SportsCenter import SportCenter
from Time.ScheduledTime import DayPeriods, ScheduledTime
from Info.PersonalInfo import PersonalInfo

class DaanSporetsCenter(SportCenter):
    def __init__(self, time, info):
        SportCenter.__init__(self, time, info)
        self.court = 6
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://scr.cyc.org.tw/tp03.aspx?module=login_page&files=login&PT=1')
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
                courts.append('//tbody/tr[' + str(2 + time * self.court + i) + ']/td[' + str(td) + ']/img[1]')
            if len(courts) >= self.scheduledTime.court:
                emptyCourts.append(courts)
        return emptyCourts

    def formatTime(self) :
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
        return startTime, endTime

    # TODO : try & except
    def run(self):
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
        WebDriverWait(self.driver, 100).until(lambda driver: len(self.driver.find_element(By.XPATH, '//*[@id=\"ContentPlaceHolder1_Captcha_text\"]').get_attribute("value")) == 5)
        self.driver.find_element(By.XPATH, '//*[@id=\"login_but\"]').click()
        self.driver.find_element(By.XPATH, '//*[@title=\"羽球\"]').click()
        self.driver.find_element(By.XPATH, '//*[@src=\"img/conf01.png\"]').click()
        self.alert.accept()
        self.driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + brookingDay+ '\',1)\"]').click()

        startTime, endTime = self.formatTime()
        
        emptyCourts = self.findEmptyCourt(startTime, endTime)
        if len(emptyCourts) < self.scheduledTime.hours:
            print("Not enough courts !!")
            return
            # raise BaseException("Not enough courts !!" + str(len(emptyCourts)))

        for time in range(self.scheduledTime.hours):
            for court in range(self.scheduledTime.court):
                if(time != 0 or court != 0) : 
                    self.driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + brookingDay+ '\',1)\"]').click()
                    startTime, endTime = self.formatTime()
                self.driver.find_element(By.XPATH, emptyCourts[time][court]).click()
                self.alert.accept()
                # loading
                self.driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Step3Info_lab"]/span[2]/a[3]').click()
        print('finish')
# //*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[25]/td[3]/img
if __name__ == '__main__':
    year = 2022
    month = input()
    day = input()
    time = ScheduledTime(year, month, day, 0, 0)
    personalInfo = PersonalInfo('A000000000', '123456')
    center = YongheSportCenter(time, personalInfo)
    center.fakeRun()