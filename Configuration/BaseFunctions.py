import inspect
import os
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# utils.py

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait



def element_fail(self, locatorType, locator):
    try:
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locatorType, locator)))
    except TimeoutException:
        take_screenshot(self)
    except NoSuchElementException:
        take_screenshot(self)

def take_screenshot(self, method=None):
    if method is None:
        method = inspect.stack()[2].function
        file_name = f"C:\\Users\\10132593\\PycharmProjects\\TestOtomasyonProje2\\Screenshot\\Screenshoot_{method}.png"
        self.driver.save_screenshot(file_name)
    else:
        method = inspect.stack()[1].function
        file_name = f"C:\\Users\\10132593\\PycharmProjects\\TestOtomasyonProje2\\Screenshot\\Screenshoot_{method}.png"
        self.driver.save_screenshot(file_name)
    print(f"Ekran görüntüsü '{file_name}' olarak kaydedildi.")
