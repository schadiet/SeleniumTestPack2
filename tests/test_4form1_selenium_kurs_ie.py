import unittest

from selenium import webdriver

from pages.seleniumkurs_home_page import SeleniumKursHomePage
from pages.seleniumkurs_login_page import SeleniumKursLoginPage
from pages.seleniumkurs_test_app_page import SeleniumKursTestAppPage
from pages.seleniumkurs_testform1_page import SeleniumKursTestForm1Page


class TestForm1SeleniumKursIE(unittest.TestCase):

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

    def test_form1(self):
        print("Starte test_testform1 ")

        ##Arrange

        # Login
        loginPage = SeleniumKursLoginPage(self.driver)
        loginPage.zugangsdaten_eingeben("selenium101", "codingsolo")
        loginPage.login_button_anklicken()
        # Navigation durch das Portal
        homePage = SeleniumKursHomePage(self.driver)
        homePage.hauptmenu_aufrufen()
        homePage.selenium_test_app_anklicken()

        testAppPage = SeleniumKursTestAppPage(self.driver)
        testAppPage.test_form1_anklicken()

        # Starte Formular
        testForm1Page = SeleniumKursTestForm1Page(self.driver)
        testForm1Page.betreff_eingeben("Automatischer Test")
        testForm1Page.name_eingeben("Dieter")

        testForm1Page.kurs_auswaehlen("Java Grundlagen Kurs mit Dieter")

        testForm1Page.firma_in_box1_auswaehlen([2, 4, 6])
        testForm1Page.firmen_uebernehmen()

        testForm1Page.firma_in_box2_auswaehlen([2])

        testForm1Page.ausgewaehlte_firmen_nach_oben_verschieben()

        ##Act

        testForm1Page.formular_speichern()

        ##Assert

        erfolgsmeldung = testForm1Page.statusmeldung_auslesen()
        self.assertTrue("Java Grundlagen Kurs" in erfolgsmeldung)

        erstesElement = testForm1Page.erstes_lsitenelement_auslesen()
        self.assertEqual(erstesElement, "Magazzini Alimentari Riuniti")

    if __name__ == '__main__':
        unittest.main()
