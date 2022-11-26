from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from SportsCenterState.PickCourtState import PickCourtState
from Time.ScheduledTime import DayPeriods
from Center.SportsCenter import SportsCenter
from SportsCenterState.EndState import EndState
import Content.Content as Content
class CalculateEmptyCourtsState(State):
    # TODO : calculate continuous time courts
    def handle(self, content : Content.Content):
        content.getLock().acquire()
        if not content.getCenter().isCount():
            content.getCenter().setCount(True)   
            self.checkAvailableCourt(content)
            self.pickTargetCourt(content)
        content.getLock().release()
        if content.getCenter().getTargetCourts():
            content.setState(PickCourtState())
        else :
            print("Not enough courts !!")
            content.setState(EndState())
        content.handle()
        
    def checkAvailableCourt(self, content : Content.Content):
        driver = content.getDriver()
        emptyCourts = content.getCenter().getEmptyCourts()
        for courts in emptyCourts:
            self.selectPeriod(driver, courts[0].getTime())
            length = len(courts)
            for i in range(length - 1, -1, -1):
                if "alert" in driver.find_element(By.XPATH, courts[i].getXPath()).get_attribute("onclick"):
                    courts.pop(i)

    def pickTargetCourt(self, content : Content.Content):
        needCourt = content.getTime().getOrderCourts()
        needTime = content.getTime().getOrderTime()
        emptyCourts = content.getCenter().getEmptyCourts()
        targetCourts = content.getCenter().getTargetCourts()
        length = len(emptyCourts)
        continueCount = needTime
        for i in range(length):
            if len(emptyCourts[i]) >= needCourt:
                continueCount -= 1
            else :
                continueCount = needCourt
            if continueCount == 0:
                for j in range(i - needTime + 1, i + 1):
                    for k in range(needCourt):
                        targetCourts.append(emptyCourts[j].pop())
                break
        emptyCourts = []

    def selectPeriod(self, driver, period):
        if period >= 18:
            driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[3]').click()
        elif period >= 12:
            driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[2]').click()
        else : 
            driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[1]').click()

    
   

