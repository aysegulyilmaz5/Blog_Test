import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from PageObjectModels.EditBlog import EditBlog
from PageObjectModels.LoginPageObjectModels import LoginPageObjectModels

@pytest.mark.run(order=2)
class TestEditBlog:
    def test_edit_blog(self,setup):
        self.driver = setup
        self.driver.get("https://www.blogger.com/about/?bpli=1")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lg = LoginPageObjectModels(self.driver)
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

        self.eb = EditBlog(self.driver)
        self.eb.click_post()
        sleep(5)
        self.eb.switch_to_iframe()
        sleep(3)
        self.eb.access_image()
        sleep(3)
        self.eb.access_textbox("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
        sleep(3)
        self.eb.default_content()
        sleep(3)
        self.eb.addtitle("Editted Blog")
        sleep(3)
        self.eb.click_update()
        sleep(3)
        self.eb.click_review_button()
        sleep(3)

        self.driver.quit()

