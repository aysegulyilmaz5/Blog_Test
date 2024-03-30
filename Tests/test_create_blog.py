import pytest
from Configuration import config
import logging

from time import sleep

from Pages.CreateBlog import CreateBlog
from Pages.LoginPageObjectModels import LoginPageObjectModels

logger = logging.getLogger(__name__)
@pytest.mark.run(order=1)
class TestCreateBlog:

    """Test case is:
        1.Open Browser
        2.Click Login Button
        3.Enter email
        4.Click next button
        5.Enter password
        6.Click next button
        7.Open blog
        8.Click picture icon
        9.Click url plaintext
        10.Switch frame & paste url
        11.Click select button
        12.Switch default content
        13.Click publish button
        14.Click confirm button
        15.Close browser"""

    def test_create_blog(self,setup):
        self.driver = setup

        filehandler = logging.FileHandler(filename="example.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        main_url = config.main_page_url
        logger.info("1.Browser opened successfully visit blogger.com")
        self.driver.get(main_url)

        logger.info("2. Maximized window")
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

        self.lg = LoginPageObjectModels(self.driver)
        self.cbl = CreateBlog(self.driver)

        adm_email = config.admin_email
        adm_passwordd = config.admin_password

        logger.info("3.Clicked login")
        self.lg.clickLogin()


        logger.info("4.Email entered successfully")
        self.lg.setEmail(adm_email)


        logger.info("5.Clicked next button")
        self.lg.clicknext()


        logger.info("6. Password entered successfully")
        self.lg.setPassword(adm_passwordd)


        logger.info("7. Clicked next button")
        self.lg.clicksecondnext()


        logger.info("8.Opened blog")
        self.cbl.button_blog()


        logger.info("9.Clicked picture icon")
        self.cbl.picture()



        logger.info("10.Clicked url plaintext")
        self.cbl.url_download()


        picture_url = config.create_blog_picture_url
        logger.info("11. Switch frame & Downloading url")
        self.cbl.file_download(picture_url)


        logger.info("12. Url entered successfully")
        self.cbl.select_button()


        logger.info("13. Switch default content")
        self.cbl.default_content()


        logger.info("14.Clicked publish button")
        self.cbl.publish_blog()


        logger.info("15. Clicked confirm button")
        self.cbl.confirm_button()


        logger.info("16.Browser closed successfully")
        self.tearDown()

    def tearDown(self):
        self.driver.close()


