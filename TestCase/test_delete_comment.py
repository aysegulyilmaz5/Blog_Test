import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from PageObjectModels.AdminDeleteComment import AdminDeleteComment
from PageObjectModels.CreateBlog import CreateBlog
from PageObjectModels.LoginPageObjectModels import LoginPageObjectModels

@pytest.mark.run(order=4)
class TestDeleteComment:
    def test_delete_comment(self,setup):
        self.driver = setup
        self.driver.get("https://www.blogger.com/about/?bpli=1")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lg = LoginPageObjectModels(self.driver)
        self.dc = AdminDeleteComment(self.driver)
        self.lg.clickLogin()
        sleep(3)
        self.lg.setEmail("gmail")
        sleep(3)
        self.lg.clicknext()
        sleep(3)
        self.lg.setPassword("password")
        sleep(3)
        self.lg.clicksecondnext()
        sleep(3)
        self.dc.view_blog()
        sleep(3)
        self.dc.click_test()
        sleep(3)
        self.dc.click_delete()
        sleep(3)
        self.dc.accept_delete()
        sleep(3)

        self.driver.quit()
