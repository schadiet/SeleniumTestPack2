import unittest

from selenium import webdriver

from pages.seleniumkurs_home_page import SeleniumKursHomePage
from pages.seleniumkurs_login_page import SeleniumKursLoginPage
from pages.seleniumkurs_test_app_page import SeleniumKursTestAppPage
from pages.seleniumkurs_testform1_page import SeleniumKursTestForm1Page


class TestNavigationSeleniumKursIE(unittest.TestCase):

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

    def test_navigation(self):
        print("Starte test_navigation ")

        ##Arrange

        loginPage = SeleniumKursLoginPage(self.driver)
        loginPage.zugangsdaten_eingeben("selenium101", "codingsolo")
        loginPage.login_button_anklicken()

        ##Act

        homePage = SeleniumKursHomePage(self.driver)
        homePage.hauptmenu_aufrufen()
        homePage.selenium_test_app_anklicken()

        testAppPage = SeleniumKursTestAppPage(self.driver)
        testAppPage.test_form1_anklicken()

        ##Assert

        testForm1Page = SeleniumKursTestForm1Page(self.driver)

        erfolgsmeldung = testForm1Page.ueberschrift_auselsen()
        self.assertEqual(erfolgsmeldung,"Selenium Test Form1")

    if __name__ == '__main__':
        unittest.main()
