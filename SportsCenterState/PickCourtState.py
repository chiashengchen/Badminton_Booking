from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from Center.SportsCenter import SportsCenter
import SportsCenterState.MainPageState as Main
from SportsCenterState.EndState import EndState
import Content.Content as Content

class PickCourtState(State):
    def handle(self, content : Content.Content):
        driver = content.getDriver()
        lock = content.getLock()
        alert = Alert(driver)
        lock.acquire()
        targetCourts = content.getCenter().getTargetCourts()
        for court in targetCourts:
            self.selectPeriod(driver, court.getTime())
            if "alert" in driver.find_element(By.XPATH, court.getXPath()).get_attribute("onclick"):
                print("[EMPTY COURT TIME AT " + str(court.getTime()) + " ]")
                targetCourts.remove(court)
                continue
            driver.find_element(By.XPATH, court.getXPath()).click()
            tmpCourt = court
            targetCourts.remove(court)
            alert.accept()
            break
        lock.release()
        if not targetCourts:
            content.setState(EndState())
        else:
            try:
                driver.find_element(By.XPATH, '//*[@id=\"ContentPlaceHolder1_Step3Info_lab\"]/span[2]/a[1]').click()
                print("[PICK] Pick court " + str(tmpCourt.getTime()))
            except:
                print("[ORDERING ERROR]")
                driver.find_element(By.XPATH, '/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr/td/a[1]/span').click()
                targetCourts.append(tmpCourt)
        content.handle()

    def selectPeriod(self, driver, period):
        if period >= 18:
            driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[3]').click()
        elif period >= 12:
            driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[2]').click()
        else : 
            driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[1]').click()