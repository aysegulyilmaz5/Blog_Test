from enum import Enum

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from Configuration import config
from Configuration.BaseFunctions import element_fail
from time import sleep

#deneme3
class EditBlog:
    # Locators
    click_post_xpath = "//div[contains(@class, 'LgQiCc') and contains(@class, 'vOSR6b') and contains(@class, 'oqIa7e')]"
    textBoxView_xpath = "//body[@role='textbox']"
    image_xpath = "//img[@data-original-height='145']"
    title_box_xpath = "(//input[@aria-label='Başlık'])[1]"
    update_button_xpath = "//div[@aria-label='Güncelle']//div[@class='A2yzVd']"

    # Variables

    text = config.text
    example_title = config.example_title
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def click_post(self):
        """Click to created post"""
        element_fail(self,"xpath",self.click_post_xpath)
        self.driver.find_element(By.XPATH,self.click_post_xpath).click()

    def switch_to_iframe(self):
        """Switch to post iframe"""
        sleep(3)
        iframe = self.driver.find_element(By.CSS_SELECTOR,"iframe[class='ZW3ZFc editable']")
        self.driver.switch_to.frame(iframe)

    def access_image(self):
        """Resize image in blog"""
        element_fail(self,"xpath",self.image_xpath)
        image = self.driver.find_element(By.XPATH,self.image_xpath)
        self.driver.execute_script("arguments[0].style.height = '600px'; arguments[0].style.width = '600px';",image)

    def access_textbox(self, text):
        """Add text to textbox:
            param str text:Text you want to enter"""
        element_fail(self, "xpath", self.textBoxView_xpath)
        textbox = self.driver.find_element(By.XPATH, self.textBoxView_xpath)
        textbox.send_keys(text)

    def default_content(self):
        """Switch to default content to quit iframe"""
        sleep(3)
        self.driver.switch_to.default_content()

    def addtitle(self,example_title):
        """Enter title to title box:
            param str index:Title you want to enter"""
        element_fail(self,"xpath",self.title_box_xpath)
        title = self.driver.find_element(By.XPATH,self.title_box_xpath)
        title.send_keys(example_title)

    def click_update(self):
        """Click update button"""
        element_fail(self,"xpath",self.update_button_xpath)
        self.driver.find_element(By.XPATH,self.update_button_xpath).click()












