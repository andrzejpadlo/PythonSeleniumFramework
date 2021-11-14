from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryWindow = (By.ID, "country")
    pol = (By.LINK_TEXT, "Poland")
    purchaseBtn = (By.CSS_SELECTOR, "input.btn")
    successAlert = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    @property
    def inputCountry(self):
        return self.driver.find_element(*ConfirmPage.countryWindow)

    @property
    def selectPoland(self):
        return self.driver.find_element(*ConfirmPage.pol)

    @property
    def purchaseItem(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    @property
    def getAlert(self):
        return self.driver.find_element(*ConfirmPage.successAlert)
