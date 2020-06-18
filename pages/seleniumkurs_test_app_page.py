from selenium.webdriver.common.by import By


class SeleniumKursTestAppPage:
    BTN_HAUPTMENU = (By.ID, "portaltab-burger-menu")
    LINK_TESTFORM1 = (By.LINK_TEXT, "Selenium Test Form1")
    LINK_DragAndDrop = (By.LINK_TEXT, "Drag and Drop Beispiel")
    LINK_IFRAMEBEISPIEL = (By.LINK_TEXT, "IFrame Beispiel")
    LINK_WEBELEMENTE = (By.LINK_TEXT, "Web Elemente")
    LINK_KATZENSUCHE = (By.LINK_TEXT ,"Katzensuche Testseite (AJAX)")

    def __init__(self, driver):
        self.driver = driver

    def hauptmenu_aufrufen(self):
        self.driver.find_element(*self.BTN_HAUPTMENU).click()

    def test_form1_anklicken(self):
        self.driver.find_element(*self.LINK_TESTFORM1).click()

    def drag_and_drop_anklicken(self):
        self.driver.find_element(*self.LINK_DragAndDrop).click()

    def iframe_beispiel_anklicken(self):
        self.driver.find_element(*self.LINK_IFRAMEBEISPIEL).click()

    def web_elemente_anklicken(self):
        self.driver.find_element(*self.LINK_WEBELEMENTE).click()

    def katzensuche_anklicken(self):
        self.driver.find_element(*self.LINK_KATZENSUCHE).click()