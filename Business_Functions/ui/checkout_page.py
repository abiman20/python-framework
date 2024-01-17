from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout_page:

    def __init__(self,browser) -> None:
        self.browser: webdriver.Chrome = browser
        self.first_name = "first-name"
        self.last_name = "last-name"
        self.zip_code = "postal-code"


    def checkout_item(self):
        self.browser.find_element(By.ID, "checkout").click()
    
    def verify_checkout_page(self):
        checkout_page ="https://www.saucedemo.com/checkout-step-one.html"
        assert self.browser.current_url == checkout_page, self.browser.current_url +' is not equal to ' + checkout_page
    
    def checkout_information(self,first_name,last_name,zip_code):
        self.browser.find_element(By.ID, self.first_name).send_keys(first_name)
        self.browser.find_element(By.ID, self.last_name).send_keys(last_name)
        self.browser.find_element(By.ID, self.zip_code).send_keys(zip_code)
        self.browser.find_element(By.ID, "continue").click()

    def checkout_step_two(self):
        checkout_next_step = "https://www.saucedemo.com/checkout-step-two.html"
        assert self.browser.current_url == checkout_next_step, self.browser.current_url +' is not equal to ' + checkout_next_step
        self.browser.find_element(By.ID, "finish").click()

