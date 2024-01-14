from selenium import webdriver # UI automation tool
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Product_page:
    
    def __init__(self, browser) -> None:
        self.browser: webdriver.Chrome = browser
    
    def verify_product_page(self):
        product_page = "https://www.saucedemo.com/inventory.html"
        assert self.browser.current_url == product_page, self.browser.current_url +' is not equal to ' + product_page
        title = self.browser.find_element(By.XPATH,'//div[contains(text(),"Swag Labs")]').text
        assert title == "Swag Labs", title
        self.browser.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
        WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@id='logout_sidebar_link']")))
        self.browser.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()