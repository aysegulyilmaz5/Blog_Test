import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

from PageObjectModels.CheckDeletedComments import CheckDeletedComments
from PageObjectModels.EditBlog import EditBlog
from PageObjectModels.GuestOperations import GuestOperations
from PageObjectModels.LoginPageObjectModels import LoginPageObjectModels


# g10858167@gmail.com
# Ntt123456.
@pytest.mark.run(order=5)
class TestGuestOperations:
    def test_check_deleted_comments(self,setup):
        self.driver = setup
        self.driver.get("https://testotomasyoncase2.blogspot.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


        self.pv = GuestOperations(self.driver)

        assert self.pv.post_visibility()






