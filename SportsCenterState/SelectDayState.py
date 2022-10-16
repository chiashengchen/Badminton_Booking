from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from SportsCenterState.CalculateEmptyCourtsState import CalculateEmptyCourtsState
from SportsCenterState.SelectPeriod import SelectPeriod
from selenium.common.exceptions import NoSuchElementException
import time
import Content.Content as Content

class SelectDayState(State):
    def handle(self, content : Content.Content):
        driver = content.getDriver()
        try:
            # center.driver.find_element(By.XPATH, '//td[contains(text(),\''+ str(center.time.day) + '\')]').click()
            driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + content.getTime().getScheduledDate() + '\',1)\"]').click()
            content.setState(CalculateEmptyCourtsState())
        except NoSuchElementException:
            # TODO 那天的場已經訂滿了
            print("error and refresh")
            time.sleep(10)
            driver.refresh()
            content.setState(SelectDayState())
        content.handle()
        # //*[@id="ContentPlaceHolder1_Date_Lab"]/table/tbody/tr[5]/td[6]/table/tbody/tr[2]/td
        # //*[@id="ContentPlaceHolder1_Date_Lab"]/table/tbody/tr[5]/td[7]/table/tbody/tr[1]/td
        # //*[@id="ContentPlaceHolder1_Date_Lab"]/table/tbody/tr[6]/td[7]/table/tbody/tr[2]/td

        # //td[contains(text(),'26')]