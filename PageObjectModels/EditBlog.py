from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pyperclip

class EditBlog:

    # Locators
    click_post_css = ".LgQiCc.vOSR6b.oqIa7e"
    textBoxView_xpath = "//body[@role='textbox']"
    image_xpath = "//img[@data-original-height='145']"
    title_box_xpath = "(//input[@aria-label='Başlık'])[1]"
    update_button_css = "div[aria-label='Güncelle'] div[class='A2yzVd']"
    review_button_css = "div[aria-label='Yayını önizle'] span[class='CwaK9']"

    # Variables
    text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    example_title = "Editted Blog"
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def click_post(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_post_css).click()

    def switch_to_iframe(self):
        iframe = self.driver.find_element(By.CSS_SELECTOR, "iframe[class='ZW3ZFc editable']")
        self.driver.switch_to.frame(iframe)

    def access_image(self):
        image = self.driver.find_element(By.XPATH, self.image_xpath)
        self.driver.execute_script("arguments[0].style.height = '600px'; arguments[0].style.width = '600px';", image)

    def access_textbox(self,text):
        textbox = self.driver.find_element(By.XPATH,self.textBoxView_xpath)
        textbox.send_keys(text)

    def default_content(self):
        self.driver.switch_to.default_content()

    def addtitle(self,example_title):
        title = self.driver.find_element(By.XPATH,self.title_box_xpath)
        title.send_keys(example_title)

    def click_update(self):
        self.driver.find_element(By.CSS_SELECTOR,self.update_button_css).click()

    def click_review_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.review_button_css).click()










