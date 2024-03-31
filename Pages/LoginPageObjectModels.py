from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pyperclip
from time import sleep
from Configuration import config
from Configuration.BaseFunctions import element_fail


class LoginPageObjectModels:
    #Locators
    button_login = "//a[@class='sign-in ga-header-sign-in']"
    txtbox_email_xpath = "//input[@name='identifier']"
    txtbox_password_xpath = "//input[@name='Passwd']"
    button_next_id = "identifierNext"
    button_second_next = "passwordNext"



    #Constructor
    def __init__(self, driver):
        self.driver = driver

    #Actions
    def setEmail(self, email):
        """Gets user email to log in:
        param str index:User email you want to Login with"""
        element_fail(self,"xpath",self.txtbox_email_xpath)
        element = self.driver.find_element(By.XPATH,self.txtbox_email_xpath)
        element.send_keys(email)


    def setPassword(self, pwd):
        """Gets user password to log in:
        param str index:User password you want to Login with"""
        element_fail(self,"xpath",self.txtbox_password_xpath)
        element = self.driver.find_element(By.XPATH,self.txtbox_password_xpath)
        element.send_keys(pwd)

    def clickLogin(self):
        """Click login button to use user credentials to Login"""
        element_fail(self,"xpath",self.button_login)
        element = self.driver.find_element(By.XPATH,self.button_login)
        element.click()
    def clicknext(self):
        """Click next button to switch password page"""
        self.driver.find_element(By.ID,self.button_next_id).click()


    def clicksecondnext(self):
        """Click next button to log in"""
        self.driver.find_element(By.ID,self.button_second_next).click()



