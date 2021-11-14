from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name_input = (By.CSS_SELECTOR, "input[name='name']")
    email_input = (By.NAME, "email")
    icecream_checkbox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit_button = (By.XPATH, "//input[@type='submit']")
    success_info = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    @property
    def getName(self):
        return self.driver.find_element(*HomePage.name_input)

    @property
    def getEmail(self):
        return self.driver.find_element(*HomePage.email_input)

    @property
    def getCheckbox(self):
        return self.driver.find_element(*HomePage.icecream_checkbox)

    @property
    def getGender(self):
        return self.driver.find_element(*HomePage.dropdown)

    @property
    def submitForm(self):
        return self.driver.find_element(*HomePage.submit_button)

    @property
    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.success_info)
