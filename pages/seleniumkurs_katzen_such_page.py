from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SeleniumKursKatzenSuchPage:

    TEXT_BESCHREIBUNG = (By.CSS_SELECTOR, "p.lead")
    IMG_KATZE1 = (By.ID, "WTQSRMJOY")
    IMG_KATZE2 = (By.ID, "29RH1pQb5")
    LINK_NEXT = (By.LINK_TEXT, "Next")
    LINK_PREVIOUS = (By.LINK_TEXT, "Previous")
    SELECT_ANZAHL = (By.ID, "anzahlSelect")


    def __init__(self, driver):
        self.driver = driver

    def beschreibung_auslesen(self):
        return self.driver.find_element(*self.TEXT_BESCHREIBUNG).text

    def sourcelink_katze1_auslesen(self):
        return self.driver.find_element(*self.IMG_KATZE1).get_attribute("src")

    def sourcelink_katze2_auslesen(self):
        return self.driver.find_element(*self.IMG_KATZE2).get_attribute("src")

    def eine_seite_weiter_klicken(self):
        self.driver.find_element(*self.LINK_NEXT).click()

    def eine_seite_zurueck_klicken(self):
        self.driver.find_element(*self.LINK_PREVIOUS).click()

    def anzahl_eingeben(self, anzahl):
        anzahl_auswahl = Select(self.driver.find_element(*self.SELECT_ANZAHL))
        anzahl_auswahl.select_by_value(anzahl)