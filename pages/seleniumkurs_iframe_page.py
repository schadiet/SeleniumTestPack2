from selenium.webdriver.common.by import By


class SeleniumKursIFramePage:

    INPUT_NAME = (By.ID, "name")
    BTN_ALERT = (By.ID, "alertbtn")

    def __init__(self, driver):
        self.driver = driver


    def aktiviere_iframe(self):
        self.driver.switch_to.frame("iframe")

    def namen_eingeben(self, namen):
        self.driver.find_element(*self.INPUT_NAME).send_keys(namen)

    def alert_anklicken(self):
        self.driver.find_element(*self.BTN_ALERT).click()

    def alert_box_auslesen(self):
        return self.driver.switch_to.alert.text

    def alert_box_wegklicken(self):
        self.driver.switch_to.alert.accept()
