import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


from PageObjectModels.CheckDeletedPost import CheckDeletedPost
from PageObjectModels.EditBlog import EditBlog
from PageObjectModels.GuestOperations import GuestOperations
from PageObjectModels.LoginPageObjectModels import LoginPageObjectModels


# g10858167@gmail.com
# Ntt123456.
@pytest.mark.run(order=6)
class TestGuestOperations:
    def test_check_deleted_posts(self,setup):
        self.driver = setup
        self.driver.get("https://www.blogger.com/blog/posts/432056193280063588")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lg = LoginPageObjectModels(self.driver)

        self.lg.setEmail("gmail")
        sleep(3)
        self.lg.clicknext()
        sleep(3)
        self.lg.setPassword("password")
        sleep(3)
        self.lg.clicksecondnext()
        sleep(3)

        self.cdp = CheckDeletedPost(self.driver)
        pre_count = self.cdp.pre_post_count()
        sleep(3)
        self.cdp.delete_post()
        sleep(3)
        post_count = self.cdp.post_post_count()

        if pre_count - post_count == 1:
            assert True
        else:
            assert False

        self.driver.quit()





