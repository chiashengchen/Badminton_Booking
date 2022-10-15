from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from Time.ScheduledTime import DayPeriods
from SportsCenterState.JhongJhengState.CalculateEmptyCourtsState import CalculateEmptyCourtsState

class SelectPeriod(State):
    def handle(self, center):
        if center.time.getCalendarDayPeriods() == DayPeriods.AFTERNOON:
            center.driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[2]').click()
            
        elif center.time.getCalendarDayPeriods() == DayPeriods.EVENING:
            center.driver.find_element(By.XPATH, '//tbody/tr[2]/td[1]/span[1]/div[3]').click()
        center.setState(CalculateEmptyCourtsState())
        center.handle()