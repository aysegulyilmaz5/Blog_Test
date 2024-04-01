import pytest
from Configuration import config
import logging
from time import sleep

from Pages.EditBlog import EditBlog
from Pages.LoginPageObjectModels import LoginPageObjectModels

logger = logging.getLogger(__name__)
@pytest.mark.run(order=2)
class TestEditBlog:
    """Test Case is:
        1.Open Browser
        2.Click login button
        3.Enter email
        4.Click next button
        5.Enter password
        6.Click next button
        7.Click post
        8.Switch to iframe
        9.Select image and resize image
        10.Enter text to iframe
        11.Switch to default content
        12.Enter title to post
        13.Click update button
        14.Close Browser"""
    def test_edit_blog(self,setup):
        self.driver = setup

        filehandler = logging.FileHandler(filename="example.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        main_url = config.main_page_url
        logger.info("1.Browser opened successfully")
        self.driver.get(main_url)

        logger.info("2.Maximized window")
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

        self.lg = LoginPageObjectModels(self.driver)

        adm_email = config.admin_email
        adm_passwordd = config.admin_password

        logger.info("3.Clicked login button")
        self.lg.clickLogin()


        logger.info("4.Email entered successfully")
        self.lg.setEmail(adm_email)


        logger.info("5.Clicked next button")
        self.lg.clicknext()


        logger.info("6.Password entered successfully")
        self.lg.setPassword(adm_passwordd)


        logger.info("7.Clicked next button")
        self.lg.clicksecondnext()


        self.eb = EditBlog(self.driver)

        logger.info("8.Clicked post")
        self.eb.click_post()


        logger.info("9.Switched to iframe")
        self.eb.switch_to_iframe()


        logger.info("10.Select image and resize image")
        self.eb.access_image()


        logger.info("11. Entered text to iframe")
        text = config.text
        self.eb.access_textbox(text)


        logger.info("12. Switch to default content")
        self.eb.default_content()


        logger.info("13. Entered title to post")
        example_title = config.example_title
        self.eb.addtitle(example_title)


        logger.info("14.Clicked update button")
        self.eb.click_update()

        logger.info("16. Browser closed successfully")
        self.tearDown()

    def tearDown(self):
        self.driver.close()

