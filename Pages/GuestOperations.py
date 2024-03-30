from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pyperclip

class GuestOperations:
    # Locators
    view_blog_xpath = "(//div[@class='weDT4c'])[2]"
    add_comment_css = "span[class='num_comments'"
    new_comment= "textarea[aria-label='Yorum Girin']"
    sign_in_google = "div[aria-label='Google ile oturum aç'] span[class='RveJvd snByac']"
    publish_button = "div[aria-label='Yayınla']"
    featured_post_id = "FeaturedPost1"
    #Variables
    example_comment = "Successed Test"


    def __init__(self, driver):
        self.driver = driver

    def post_visibility(self):
        """Checks the post visibility:
            return bool:Return true if post visible"""
        post = self.driver.find_element(By.ID,self.featured_post_id)
        return bool(post)

    def add_comment(self):
        """Click to add comment button"""
        self.driver.find_element(By.CSS_SELECTOR, self.add_comment_css).click()

    def click_google(self):
        """Click to open with google button"""
        self.driver.find_element(By.CSS_SELECTOR,self.sign_in_google).click()

    def switch_iframe(self):
        """Switch to post iframe"""
        iframe = self.driver.find_element(By.NAME, "comment-editor")
        self.driver.switch_to.frame(iframe)

    def enter_comment(self,example_comment):
        """Enter comment text to comment box:
            param str index:Comment text you want to enter"""
        comment_box = self.driver.find_element(By.CSS_SELECTOR,self.new_comment)
        comment_box.send_keys(example_comment)

    def publish(self):
        """Click publish button"""
        self.driver.find_element(By.CSS_SELECTOR,self.publish_button).click()









