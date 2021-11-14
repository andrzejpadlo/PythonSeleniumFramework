import pytest
import logging
import inspect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, locator, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((locator, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fhand = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fhand.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(fhand)

        logger.setLevel(logging.DEBUG)
        return logger
