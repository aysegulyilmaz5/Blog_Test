from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pyperclip
from Configuration.BaseFunctions import element_fail,take_screenshot
from time import sleep
class GuestOperations:
    # Locators
    view_blog_xpath = "(//div[@class='weDT4c'])[2]"
    add_comment_xpath = "//span[@class='num_comments']"
    new_comment_xpath= "//textarea[@aria-label='Yorum Girin']"
    sign_in_google_xpath = "//div[@aria-label='Google ile oturum aç']//span[@class='RveJvd snByac']"
    publish_button_xpath = "//div[@aria-label='Yayınla']"
    featured_post_xpath = "//div[@id='FeaturedPost1']"

    #Variables
    example_comment = "Successed Test"


    def __init__(self, driver):
        self.driver = driver

    def post_visibility(self):
        """Checks the post visibility:
            return bool:Return true if post visible"""
        element_fail(self,"xpath",self.featured_post_xpath)
        post = self.driver.find_element(By.XPATH,self.featured_post_xpath)
        return bool(post)

    def add_comment(self):
        """Click to add comment button"""
        element_fail(self,"xpath",self.add_comment_xpath)
        self.driver.find_element(By.XPATH, self.add_comment_xpath).click()

    def click_google(self):
        """Click to open with google button"""
        element_fail(self,"xpath",self.sign_in_google_xpath)
        self.driver.find_element(By.XPATH,self.sign_in_google_xpath).click()

    def switch_iframe(self):
        """Switch to post iframe"""
        sleep(1)
        iframe = self.driver.find_element(By.NAME, "comment-editor")
        self.driver.switch_to.frame(iframe)
        sleep(3)

    def enter_comment(self,example_comment):
        """Enter comment text to comment box:
            param str index:Comment text you want to enter"""
        element_fail(self,"xpath",self.new_comment_xpath)
        comment_box = self.driver.find_element(By.XPATH,self.new_comment_xpath)
        comment_box.send_keys(example_comment)

    def publish(self):
        """Click publish button"""
        element_fail(self,"xpath",self.publish_button_xpath)
        self.driver.find_element(By.XPATH,self.publish_button_xpath).click()










