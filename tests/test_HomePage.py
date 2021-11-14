import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.get_logger()
        homePage = HomePage(self.driver)
        homePage.getName.send_keys(getData["firstname"])
        homePage.getEmail.send_keys(getData["email"])
        homePage.getCheckbox.click()
        self.selectOptionByText(homePage.getGender, getData["gender"])
        homePage.submitForm.click()
        alertText = homePage.getSuccessMessage.text
        assert "Success! The Form has been submitted successfully" in alertText
        self.driver.get_screenshot_as_file("screen.png")
        self.driver.refresh()
        log.info("Name entered in this occurance: " + getData["firstname"])

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
