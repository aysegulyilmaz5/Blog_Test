import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from PageObjectModels.CreateBlog import CreateBlog
from PageObjectModels.LoginPageObjectModels import LoginPageObjectModels

@pytest.mark.run(order=1)
class TestLogin:

    def test_login(self,setup):
        self.driver = setup
        self.driver.get("https://www.blogger.com/about/?bpli=1")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lg = LoginPageObjectModels(self.driver)
        self.cbl = CreateBlog(self.driver)
        self.lg.clickLogin()
        sleep(3)
        self.lg.setEmail("ylmz.aysegl1@gmail.com")
        sleep(3)
        self.lg.clicknext()
        sleep(3)
        self.lg.setPassword("Ayseyilmaz58.")
        sleep(3)
        self.lg.clicksecondnext()
        sleep(3)

        self.cbl.button_blog()
        sleep(5)
        self.cbl.picture()
        sleep(5)
        self.cbl.url_download()
        sleep(5)
        self.cbl.file_download("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJBRaZADlwDwI2UIsll_wdST_C_6-Q8WIjMjmoNTrbDQ&s")
        sleep(5)
        self.cbl.select_button()
        sleep(5)
        self.cbl.default_content()
        sleep(5)
        self.cbl.publish_blog()
        sleep(5)
        self.cbl.confirm_button()
        sleep(5)

        self.driver.quit()


