from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        checkoutPage.addBlackberry.click()
        checkoutPage.gotoBasket.click()
        confirmPage = checkoutPage.gotoCheckout()
        confirmPage.inputCountry.send_keys("pol")
        self.verifyLinkPresence(*confirmPage.pol)
        confirmPage.selectPoland.click()
        confirmPage.purchaseItem.click()
        self.verifyLinkPresence(*confirmPage.successAlert)
        assert "Success! Thank you! Your order will be delivered" in confirmPage.getAlert.text
        log.info("Alert text is " + confirmPage.getAlert.text)
        self.driver.get_screenshot_as_file("screen.png")
