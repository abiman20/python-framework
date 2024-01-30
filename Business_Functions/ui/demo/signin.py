from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Signin_page:

    def __init__(self, browser) -> None:
        self.browser: webdriver.Chrome = browser
        self.browser.find_element(By.ID,"btn1").click()
        self.email = "//input[@placeholder='E mail']"
        self.password = "//input[@placeholder='Password']"


    def signin(self,email,password):
        #syntax for xpath = //tagname[@attribute = 'value']
        self.browser.find_element(By.XPATH, self.email).send_keys(email)
        self.browser.find_element(By.XPATH, self.password).send_keys(password)
        self.browser.find_element(By.ID, "enterbtn").click()

    