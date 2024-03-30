from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pyperclip
from time import sleep
from Configuration import config,BaseFunctions


class LoginPageObjectModels:
    #Locators
    button_login = "//a[@class='sign-in ga-header-sign-in']"
    txtbox_email_name = "identifierId"
    txtbox_password_name = "Passwd"
    button_next_id = "identifierNext"
    button_second_next = "passwordNext"


    #Constructor
    def __init__(self, driver):
        self.driver = driver

    #Actions
    def setEmail(self, email):
        """Gets user email to log in:
        param str index:User email you want to Login with"""
        try:
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, "identifierId")))
            element.send_keys(email)
            BaseFunctions.take_screenshot(self,1)
        except TimeoutException:
            print("Timed out waiting for page to load")


    def setPassword(self, pwd):
        """Gets user password to log in:
        param str index:User password you want to Login with"""
        try:
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME, self.txtbox_password_name)))
            element.send_keys(pwd)
        except TimeoutException:
            print("Timed out waiting for page to load")

    def clickLogin(self):
        """Click login button to use user credentials to Login"""
        try:
            element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))
            element.click()
        except TimeoutException:
            print("Timed out waiting for page to load")

    def clicknext(self):
        """Click next button to switch password page"""
        try:
            element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.button_next_id)))
            element.click()
        except TimeoutException:
            print("Timed out waiting for page to load")


    def clicksecondnext(self):
        """Click next button to log in"""
        try:
            element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.button_second_next)))
            element.click()
        except TimeoutException:
            print("Timed out waiting for page to load")



