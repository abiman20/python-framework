from selenium import webdriver
from selenium.webdriver.common.by import By

class Cart_page:
    def __init__(self,browser) -> None:
        self.browser = browser
    
    def verify_add_to_cart_page(self,product_name,product_description):
        cart_page = "https://www.saucedemo.com/cart.html"
        assert self.browser.current_url == cart_page, self.browser.current_url +' is not equal to ' + cart_page
        title = self.browser.find_element(By.XPATH,"//span[contains(text(),'Your Cart')]").text
        assert title == "Your Cart", title
        actual_product_name =?
        actual_product_description = ?
        assert actual_product_name == product_name, actual_product_name
        assert actual_product_description == product_description,actual_product_description
        



    
