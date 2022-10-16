
from SportsCenterState.State import State
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from SportsCenterState.SelectDayState import SelectDayState
import Content.Content as Content

class MainPageState(State):
    def handle(self, content : Content.Content):
        driver = content.getDriver()
        alert = Alert(driver)
        driver.find_element(By.XPATH, '//*[@title=\"羽球\"]').click()
        try:
            alert.accept()
        except :
            print("no alert")
        driver.find_element(By.XPATH, '//*[@src=\"img/conf01.png\"]').click()
        alert.accept()
        content.setState(SelectDayState())
        content.handle()