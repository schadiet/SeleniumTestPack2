import unittest

from selenium import webdriver

from pages.seleniumkurs_home_page import SeleniumKursHomePage
from pages.seleniumkurs_login_page import SeleniumKursLoginPage


class TestLoginSeleniumKursIE(unittest.TestCase):

    def setUp(self):
        print("Initialisiere WebDriver für den Test")
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get("https://seleniumkurs.codingsolo.de")

    def tearDown(self):
        print("Nach dem Test. Ich räume auf")
        self.driver.close()
        self.driver.quit()

    def test_login(self):
        print("Starte test_login")

        ##Arrange

        loginPage = SeleniumKursLoginPage(self.driver)
        loginPage.zugangsdaten_eingeben("selenium101","codingsolo")

        ##Act

        loginPage.login_button_anklicken()

        ##Assert

        homePage = SeleniumKursHomePage(self.driver)

        erfolgsmeldung = homePage.statusmeldung_auslesen()
        self.assertTrue('Willkommen' in erfolgsmeldung)

    if __name__ == '__main__':
        unittest.main()
