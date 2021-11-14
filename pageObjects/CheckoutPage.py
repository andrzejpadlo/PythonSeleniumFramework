from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    btnBlackberry = (By.XPATH, "//a[text()='Blackberry']/../../../div[2]/button")
    btnBasket = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    btnCheckout = (By.CSS_SELECTOR, "button.btn.btn-success")

    @property
    def addBlackberry(self):
        return self.driver.find_element(*CheckoutPage.btnBlackberry)

    @property
    def gotoBasket(self):
        return self.driver.find_element(*CheckoutPage.btnBasket)

    def gotoCheckout(self):
        self.driver.find_element(*CheckoutPage.btnCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
