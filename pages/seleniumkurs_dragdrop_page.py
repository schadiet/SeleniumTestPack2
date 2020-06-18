from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class SeleniumKursDragDropPage:
    LOGO_WHITE = (By.ID, "white-logo")
    LOGO_BLUE = (By.ID, "blue-logo")
    LOGO_RED = (By.ID, "red-logo")
    LOGO_GREEN = (By.ID, "green-logo")
    LOGO_CODING = (By.ID, "coding-logo")
    DROP_BOX = (By.ID, "droppable")
    TEXT_STATUS = (By.CSS_SELECTOR, "#droppable > p")

    def __init__(self, driver):
        self.driver = driver

    def status_abfragen(self):
        return self.driver.find_element(*self.TEXT_STATUS).text

    # Standard Drag and Drop
    def bewege_alle_logos_in_die_box(self):
        drglogo1 = self.driver.find_element(*self.LOGO_WHITE)
        drglogo2 = self.driver.find_element(*self.LOGO_BLUE)
        drglogo3 = self.driver.find_element(*self.LOGO_RED)
        drglogo4 = self.driver.find_element(*self.LOGO_GREEN)
        drglogo5 = self.driver.find_element(*self.LOGO_CODING)
        drpbox = self.driver.find_element(*self.DROP_BOX)

        action = ActionChains(self.driver)
        action.drag_and_drop(drglogo1, drpbox).perform()
        action.drag_and_drop(drglogo2, drpbox).perform()
        action.drag_and_drop(drglogo3, drpbox).perform()
        action.drag_and_drop(drglogo4, drpbox).perform()
        action.drag_and_drop(drglogo5, drpbox).perform()

    # Standard Drag and Drop
    def bewege_logowhite_in_box(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*self.LOGO_WHITE),
                             self.driver.find_element(*self.DROP_BOX)).perform()

    def bewege_logoblue_in_box(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*self.LOGO_BLUE),
                             self.driver.find_element(*self.DROP_BOX)).perform()

    def bewege_logored_in_box(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*self.LOGO_RED),
                             self.driver.find_element(*self.DROP_BOX)).perform()

    def bewege_logogreen_in_box(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*self.LOGO_GREEN),
                             self.driver.find_element(*self.DROP_BOX)).perform()

    def bewege_logocs_in_box(self):
        action = ActionChains(self.driver)
        action.drag_and_drop(self.driver.find_element(*self.LOGO_CODING),
                             self.driver.find_element(*self.DROP_BOX)).perform()

    # Drag and Drop by Offset

    def bewege_logowhite_zum_punkt(self, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*self.LOGO_WHITE), x, y).perform()

    def bewege_logoblue_zum_punkt(self, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*self.LOGO_BLUE), x, y).perform()

    def bewege_logored_zum_punkt(self, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*self.LOGO_RED), x, y).perform()

    def bewege_logogreen_zum_punkt(self, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*self.LOGO_GREEN), x, y).perform()

    def bewege_logocs_zum_punkt(self, x, y):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.driver.find_element(*self.LOGO_CODING), x, y).perform()
