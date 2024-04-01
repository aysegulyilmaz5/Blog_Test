import pytest
from Configuration import config
import logging

from Pages.GuestOperations import GuestOperations
from time import sleep

# g10858167@gmail.com
# Ntt123456.

logger = logging.getLogger(__name__)


@pytest.mark.run(order=5)
class TestCheckDeletedComments:

    """
    Test case is:
        1. Open Browser and visit blogger.com
        2. Check post visibility
        3. Close browser
    """

    def test_check_deleted_comments(self,setup):
        self.driver = setup

        filehandler = logging.FileHandler(filename="example.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        logger.info("1. Open Browser and visit blogger.com")
        url = config.url_blogspot
        self.driver.get(url)
        logger.info("2.Browser opened and url visited")

        logger.info("3. Window Maximized")
        self.driver.maximize_window()


        logger.info("4.Browser opened successfully!")


        self.pv = GuestOperations(self.driver)

        logger.info("5.Check post visibility")
        assert self.pv.post_visibility()
        sleep(1)

        logger.info("6.Browser closed successfully!")
        self.tearDown()


    def tearDown(self):
        self.driver.close()







