import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from PageObjectModels.EditBlog import EditBlog
from PageObjectModels.GuestOperations import GuestOperations
from PageObjectModels.LoginPageObjectModels import LoginPageObjectModels


# g10858167@gmail.com
# Ntt123456.
@pytest.mark.run(order=3)
class TestGuestOperations:
    def test_guest_operations(self,setup):
        self.driver = setup
        self.driver.get("https://testotomasyoncase2.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lg = LoginPageObjectModels(self.driver)
        self.vo = GuestOperations(self.driver)


        self.vo.add_comment()
        sleep(3)
        self.vo.switch_iframe()
        sleep(3)
        self.vo.click_google()
        sleep(3)

        self.lg.setEmail("g10858167@gmail.com")
        sleep(3)
        self.lg.clicknext()
        sleep(3)
        self.lg.setPassword("Ntt123456.")
        sleep(3)
        self.lg.clicksecondnext()
        sleep(3)


        self.vo.switch_iframe()
        sleep(3)
        self.vo.enter_comment("Successed Test")
        sleep(3)
        self.vo.publish()
        sleep(3)

        self.driver.quit()

