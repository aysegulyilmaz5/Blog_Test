import pytest
from selenium.webdriver.support.wait import WebDriverWait

from Configuration import config
import logging

from time import sleep


from Pages.CheckDeletedPost import CheckDeletedPost
from Pages.LoginPageObjectModels import LoginPageObjectModels

logger = logging.getLogger(__name__)
# g10858167@gmail.com
# Ntt123456.
@pytest.mark.run(order=6)
class TestCheckDeletedPosts:

    """ Test case is:
            1.Open browser and visit blogger.com
            2.Enter email
            3.Click next button
            4.Enter password
            5.Click next button
            6.Count pre-posts
            7.Delete post
            8.Count post-posts
            9.Check deleted post
            10.Close browser"""
    def test_check_deleted_posts(self,setup):
        self.driver = setup

        filehandler = logging.FileHandler(filename="example.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        delete_url = config.delete_post_url
        self.driver.get(delete_url)
        logger.info("1.Browser opened succesfully visit blogger.com")

        self.driver.maximize_window()
        logger.info("2.Browser maximized")

        self.driver.implicitly_wait(10)

        self.lg = LoginPageObjectModels(self.driver)

        adm_email = config.admin_email
        adm_passwordd = config.admin_password

        logger.info("3. Email entered successfully")
        self.lg.setEmail(adm_email)

        logger.info("4. Clicked next button")
        self.lg.clicknext()


        logger.info("5. Password entered successfully")
        self.lg.setPassword(adm_passwordd)


        logger.info("6. Clicked next button")
        self.lg.clicksecondnext()


        self.cdp = CheckDeletedPost(self.driver)

        logger.info("7. Counted pre posts")
        pre_count = self.cdp.pre_post_count()


        logger.info("8.Deleted post")
        self.cdp.delete_post()




        logger.info("9. Counted post posts")
        post_count = self.cdp.post_post_count()

        logger.info("10. Checked deleted post")
        assert pre_count == post_count - 1, "Pre count and post count are not as expected"

        logger.info("11. Browser closed successfully")
        self.tearDown()

    def tearDown(self):
        self.driver.close()





