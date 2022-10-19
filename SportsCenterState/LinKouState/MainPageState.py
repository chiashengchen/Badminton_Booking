
from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from Center.SportsCenter import SportsCenter
from SportsCenterState.LinKouState.SelectDayState import SelectDayState

class MainPageState(State):
    def handle(self, center : SportsCenter):
        alert = Alert(center.driver)
        center.driver.find_element(By.XPATH, '//*[@title=\"羽球\"]').click()
        center.driver.find_element(By.XPATH, '//*[@src=\"img/conf01.png\"]').click()
        alert.accept()
        center.setState(SelectDayState())
        center.handle()