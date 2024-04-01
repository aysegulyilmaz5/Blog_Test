import pytest
from Configuration import config
import logging

from time import sleep

from Pages.GuestOperations import GuestOperations
from Pages.LoginPageObjectModels import LoginPageObjectModels

logger = logging.getLogger(__name__)
# g10858167@gmail.com
# Ntt123456.
@pytest.mark.run(order=3)
class TestGuestOperations:
    """
    Test Case is:
        1.Open Browser visit https://testotomasyoncase2.blogspot.com/
        2.Click add comment button
        3.Switch to iframe
        4.Click login with google button
        5.Enter email
        6.Click next button
        7.Enter password
        8.Click next button
        9.Switch to iframe
        10.Enter example comment
        11.Click to publish button
        12.Close Browser
    """
    def test_guest_operations(self,setup):
        self.driver = setup

        filehandler = logging.FileHandler(filename="example.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        blogspot_url = config.url_blogspot
        logger.info("1. Browser opened succesfully visit blogger.com")
        self.driver.get(blogspot_url)

        logger.info("2. Maximized window")
        self.driver.maximize_window()


        self.vo = GuestOperations(self.driver)
        self.lg = LoginPageObjectModels(self.driver)

        logger.info("3. Clicked add comment button ")
        self.vo.add_comment()


        logger.info("4.Switched to iframe")
        self.vo.switch_iframe()

        logger.info("5.Clicked login with google button")
        self.vo.click_google()
        sleep(1)

        self.driver.switch_to.default_content()

        logger.info("6.Email entered successfully")
        self.lg.setEmail(config.guest_email)

        logger.info("7.Clicked next button")
        self.lg.clicknext()

        logger.info("8.Password entered successfully")
        self.lg.setPassword(config.guest_password)

        logger.info("9.Clicked next button")
        self.lg.clicksecondnext()
        sleep(1)

        logger.info("10.Switched to iframe")
        self.vo.switch_iframe()

        logger.info("11. Entered example comment successfully")
        sleep(1)
        example_comment = config.example_comment
        self.vo.enter_comment(example_comment)


        logger.info("12. Clicked to publish button")
        self.vo.publish()
        sleep(1)

        logger.info("13. Browser closed successfully")
        self.tearDown()

    def tearDown(self):
        self.driver.close()

