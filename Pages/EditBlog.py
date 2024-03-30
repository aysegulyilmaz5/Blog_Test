from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configuration import config


class EditBlog:

    # Locators
    click_post_css = ".LgQiCc.vOSR6b.oqIa7e"
    textBoxView_xpath = "//body[@role='textbox']"
    image_xpath = "//img[@data-original-height='145']"
    title_box_xpath = "(//input[@aria-label='Başlık'])[1]"
    update_button_css = "div[aria-label='Güncelle'] div[class='A2yzVd']"
    review_button_css = "div[aria-label='Yayını önizle'] span[class='CwaK9']"

    # Variables

    text = config.text
    example_title = config.example_title
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def click_post(self):
        """Click to created post"""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.click_post_css)))
            element.click()
        except TimeoutException:
            print("xTimed out waiting for page to load")

    def switch_to_iframe(self):
        """Switch to post iframe"""
        try:
            # Bekleme süresi için WebDriverWait kullanarak iframe'i bul
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[class='ZW3ZFc editable']"))
            )
            # iframe bulunduğunda, iframe'e geçiş yap
            self.driver.switch_to.frame(iframe)
        except NoSuchElementException as e:
            print("Iframe not found.")
            print(e)

    def access_image(self):
        """Resize image in blog"""
        try:
            # Bekleme süresi için WebDriverWait kullanarak görüntüyü bul
            image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.image_xpath))
            )
            # Görüntü bulunduğunda, boyutlarını değiştir
            self.driver.execute_script("arguments[0].style.height = '600px'; arguments[0].style.width = '600px';",
                                       image)
        except NoSuchElementException as e:
            print("Element not found while trying to access the image.")
            print(e)
            # Hata durumunda ekran görüntüsü almak için take_screenshot fonksiyonunu burada çağırabilirsiniz

    def access_textbox(self,text):
        """Add text to textbox:
            param str index:Text you want to enter"""
        textbox = self.driver.find_element(By.XPATH,self.textBoxView_xpath)
        textbox.send_keys(text)

    def default_content(self):
        """Switch to default content to quit iframe"""
        self.driver.switch_to.default_content()

    def addtitle(self,example_title):
        """Enter title to title box:
            param str index:Title you want to enter"""
        title = self.driver.find_element(By.XPATH,self.title_box_xpath)
        title.send_keys(example_title)

    def click_update(self):
        """Click update button"""
        self.driver.find_element(By.CSS_SELECTOR,self.update_button_css).click()

    def click_review_button(self):
        """Click review button"""
        self.driver.find_element(By.CSS_SELECTOR,self.review_button_css).click()










