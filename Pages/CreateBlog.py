from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Configuration.BaseFunctions import element_fail
from time import sleep
import pyperclip


class CreateBlog:


    ####
    ######
    ####denemedeneme
    button_blog_id = "(//span[@class='MIJMVe'][contains(text(),'Yeni Yayın')])[2]"
    picture_id = "(//span[@class='DPvwYc sm8sCf GHpiyd'][contains(text(),'')])[1]"
    url_download_id = "div[class='JPdR6b e5Emjc qjTEB'] span[aria-label='URL ile']"
    file_download = "//div[@class='goog-inline-block jfk-button jfk-button-standard']"
    textbox_url_xpath = "/html/body/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div/input"
    select_button_xpath = "/html/body/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[1]"
    publish_button_xpath = "//*[@id='yDmH0d']/c-wiz[2]/div/c-wiz/div/div[1]/div[2]/div[4]/span"
    confirm_button_xpath = "(//span[@class='RveJvd snByac'][normalize-space()='Onayla'])[2]"

    def __init__(self, driver):
        self.driver = driver

    def button_blog(self):
        element_fail(self, "xpath", self.button_blog_id)
        self.driver.find_element(By.XPATH, self.button_blog_id).click()

    def picture(self):
        element_fail(self, "xpath", self.picture_id)
        self.driver.find_element(By.XPATH, self.picture_id).click()

    def url_download(self):
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, self.url_download_id).click()

    def file_download(self, image_url):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "/html/body/div[11]/div[2]/div/iframe"))
        element_fail(self, "xpath", self.textbox_url_xpath)
        textbox_url = self.driver.find_element(By.XPATH, self.textbox_url_xpath)
        sleep(3)
        pyperclip.copy(image_url)
        sleep(3)
        textbox_url.send_keys(Keys.CONTROL, 'v')

    def select_button(self):
        element_fail(self, "xpath", self.select_button_xpath)
        self.driver.find_element(By.XPATH, self.select_button_xpath).click()

    def default_content(self):
        self.driver.switch_to.default_content()

    def publish_blog(self):
        element_fail(self, "xpath", self.publish_button_xpath)
        self.driver.find_element(By.XPATH, self.publish_button_xpath).click()

    def confirm_button(self):

        element_fail(self, "xpath", self.confirm_button_xpath)
        self.driver.find_element(By.XPATH, self.confirm_button_xpath).click()
