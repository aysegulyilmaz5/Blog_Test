from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import logging
import pyperclip
from Configuration import config,BaseFunctions
from Configuration.BaseFunctions import element_fail


class AdminDeleteComment:

    #Locators
    view_blog_button_xpath = "//*[@id='yDmH0d']/c-wiz/div[1]/gm-raised-drawer/div/div[2]/div/c-wiz/div[5]/span[3]/div[2]"
    successed_test_xpath = "//*[@id='yDmH0d']/c-wiz[2]/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div[1]/span/div/div/div[2]/div[2]/div/div[1]"
    delete_xpath = "//*[@id='yDmH0d']/c-wiz[2]/div[2]/div/c-wiz/div[2]/c-wiz/div/div/div/div/span/div/div/div[4]/div[3]/span/span/span"
    accept_delete_button_xpath = "//*[@id='yDmH0d']/div[4]/div/div[2]/div[2]/div[2]"
    #Variables
    #Constructors
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
    #Actions

    def view_blog(self):
        """Click comments button"""
        element_fail(self,"xpath",self.view_blog_button_xpath)
        self.driver.find_element(By.XPATH,self.view_blog_button_xpath).click()

    def click_test(self):
        """Click comment element in list"""
        element_fail(self,"xpath",self.successed_test_xpath)
        self.driver.find_element(By.XPATH,self.successed_test_xpath).click()

    def click_delete(self):
        """Click delete icon"""
        element_fail(self,"xpath",self.delete_xpath)
        self.driver.find_element(By.XPATH,self.delete_xpath).click()


    def accept_delete(self):
        """Click accept delete button"""
        element_fail(self,"xpath",self.accept_delete_button_xpath)
        self.driver.find_element(By.XPATH,self.accept_delete_button_xpath).click()




