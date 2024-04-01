from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pyperclip
from time import sleep

class CheckDeletedPost:

    deleted_post = "//*[@id='yDmH0d']/c-wiz/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div[1]/div"
    delete_icon_xpath ="(//span[@class='DPvwYc'][contains(text(),'')])[2]"
    move_to_trash_button = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[3]/div[2]/span/span"

    def __init__(self, driver):
        self.driver = driver

    def delete_post(self):
        """Come on post and click delete icon,click trash button"""
        action = ActionChains(self.driver)
        post = self.driver.find_element(By.XPATH,self.deleted_post)
        action.move_to_element(post).perform()
        sleep(3)
        self.driver.find_element(By.XPATH, self.delete_icon_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH,self.move_to_trash_button).click()

    def post_post_count(self):
        """Take posts count:
            Return number index : Post-Post count number"""
        posts = self.driver.find_elements(By.XPATH, "(//div[@class='gNK4lf'])")
        if not posts:
            post_count_second = 0
        else:
            post_count_second = len(posts)
        return post_count_second



















