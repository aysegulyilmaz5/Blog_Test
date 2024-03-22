from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import pyperclip
from time import sleep


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
        sleep(3)
        emailtxt = self.driver.find_element(By.ID, "identifierId")
        emailtxt.send_keys(email)

    def setPassword(self, pwd):
        passwordtxt = self.driver.find_element(By.NAME, self.txtbox_password_name)
        passwordtxt.clear()
        passwordtxt.send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login).click()

    def clicknext(self):
        self.driver.find_element(By.ID, self.button_next_id).click()

    def clicksecondnext(self):
        self.driver.find_element(By.ID,self.button_second_next).click()



