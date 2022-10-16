from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from Time.ScheduledTime import DayPeriods
from SportsCenterState.CalculateEmptyCourtsState import CalculateEmptyCourtsState
import Content.Content as Content

class SelectPeriod(State):
    def handle(self, content : Content.Content):
        driver = content.getDriver()
        if content.getTime().getCalendarDayPeriods() == DayPeriods.AFTERNOON:
            driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[2]').click()
            
        elif content.getTime().getCalendarDayPeriods() == DayPeriods.EVENING:
            driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[3]').click()
        content.setState(CalculateEmptyCourtsState())
        content.handle()