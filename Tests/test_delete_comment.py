import pytest
from Configuration import config
import logging

from time import sleep

from Pages.AdminDeleteComment import AdminDeleteComment
from Pages.LoginPageObjectModels import LoginPageObjectModels

logger = logging.getLogger(__name__)
@pytest.mark.run(order=4)
class TestDeleteComment:
    """
    Test Case is:
        1.Open Browser
        2.Click Login Button
        3.Enter email
        4.Click next button
        5.Enter password
        6.Click next button
        7.Click view blog button
        8.Click comment button
        9.Click delete icon
        10.Click accept delete button
        11.Close Browser
    """
    def test_delete_comment(self,setup):
        self.driver = setup

        filehandler = logging.FileHandler(filename="example.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        main_url = config.main_page_url
        logger.info("1.Browser opened successfully visited blogger.com")
        self.driver.get(main_url)

        logger.info("2.Maximized window")
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

        self.lg = LoginPageObjectModels(self.driver)
        self.dc = AdminDeleteComment(self.driver)

        adm_email = config.admin_email
        adm_passwordd = config.admin_password

        logger.info("3.Clicked login button")
        self.lg.clickLogin()


        logger.info("4. Email entered successfully")
        self.lg.setEmail(adm_email)


        logger.info("5. Clicked next button")
        self.lg.clicknext()


        logger.info("6. Password entered succesfully")
        self.lg.setPassword(adm_passwordd)


        logger.info("7. Clicked next button")
        self.lg.clicksecondnext()


        logger.info("8.Clicked view blog button")
        self.dc.view_blog()

        assert "blog" in self.driver.current_url, "Blog görüntülenemedi!"

        logger.info("9. Clicked comment button")
        self.dc.click_test()


        logger.info("10. Clicked delete icon")
        self.dc.click_delete()


        logger.info("11. Clicked accept delete button")
        self.dc.accept_delete()
        sleep(1)


        logger.info("12.Browser closed successfully")
        self.tearDown()

    def tearDown(self):
        self.driver.close()
