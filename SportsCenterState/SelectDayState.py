from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from SportsCenterState.CalculateEmptyCourtsState import CalculateEmptyCourtsState
import SportsCenterState.EndState as End
from selenium.common.exceptions import NoSuchElementException
import time
import Content.Content as Content

class SelectDayState(State):
    def handle(self, content : Content.Content):
        driver = content.getDriver()
        center = content.getCenter()
        try:
            # center.driver.find_element(By.XPATH, '//td[contains(text(),\''+ str(center.time.day) + '\')]').click()
            driver.find_element(By.XPATH, '//*[@onclick=\"GoToStep2(\'' + content.getTime().getScheduledDate() + '\',1)\"]').click()
            content.setState(CalculateEmptyCourtsState())
        except NoSuchElementException:
            if(center.isDateAvailable()):
                print("Not available")
                content.setState(End.EndState())
            else:
                while(not center.isWithin30Sec()):
                    print("Waiting")
                    time.sleep(30)
                    pass
                time.sleep(5)
                driver.refresh()
                content.setState(SelectDayState())
        content.handle()
        # //*[@id="ContentPlaceHolder1_Date_Lab"]/table/tbody/tr[5]/td[6]/table/tbody/tr[2]/td
        # //*[@id="ContentPlaceHolder1_Date_Lab"]/table/tbody/tr[5]/td[7]/table/tbody/tr[1]/td
        # //*[@id="ContentPlaceHolder1_Date_Lab"]/table/tbody/tr[6]/td[7]/table/tbody/tr[2]/td

        # //td[contains(text(),'26')]