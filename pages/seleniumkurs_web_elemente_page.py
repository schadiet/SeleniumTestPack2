from selenium.webdriver.common.by import By


class SeleniumKursWebElementePage:

    CHECK_BOX1 = (By.ID, "checkBoxOption1")
    CHECK_BOX2 = (By.ID, "checkBoxOption2")
    CHECK_BOX3 = (By.ID, "checkBoxOption3")

    RADIO_BTN1 = (By.CSS_SELECTOR, "input[value='radio1']")
    RADIO_BTN2 = (By.CSS_SELECTOR, "input[value='radio2']")
    RADIO_BTN3 = (By.CSS_SELECTOR, "input[value='radio3']")

    def __init__(self, driver):
        self.driver = driver

    def checkbox1_anklicken(self):
        self.driver.find_element(*self.CHECK_BOX1).click()

    def checkbox2_anklicken(self):
        self.driver.find_element(*self.CHECK_BOX2).click()

    def checkbox3_anklicken(self):
        self.driver.find_element(*self.CHECK_BOX3).click()

    def checkbox1_status_auslesen(self):
        return self.driver.find_element(*self.CHECK_BOX1).is_selected()

    def checkbox2_status_auslesen(self):
        return self.driver.find_element(*self.CHECK_BOX2).is_selected()

    def checkbox3_status_auslesen(self):
        return self.driver.find_element(*self.CHECK_BOX3).is_selected()

    def radio_btn1_aktivieren(self):
        self.driver.find_element(*self.RADIO_BTN1).click()

    def radio_btn2_aktivieren(self):
        self.driver.find_element(*self.RADIO_BTN2).click()

    def radio_btn3_aktivieren(self):
        self.driver.find_element(*self.RADIO_BTN3).click()

    def radio_btn1_status_auslesen(self):
        return self.driver.find_element(*self.RADIO_BTN1).is_selected()

    def radio_btn2_status_auslesen(self):
        return self.driver.find_element(*self.RADIO_BTN2).is_selected()

    def radio_btn3_status_auslesen(self):
        return self.driver.find_element(*self.RADIO_BTN3).is_selected()