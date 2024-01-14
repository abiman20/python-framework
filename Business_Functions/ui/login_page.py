from selenium import webdriver # UI automation tool
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page:
    def __init__(self, browser) -> None:
        self.browser: webdriver.Chrome = browser
        self.username = "user-name"
        self.password = "password"
    
    def login_saucelab(self, username, password):
        self.browser.find_element(By.ID, self.username).send_keys(username)
        self.browser.find_element(By.ID, self.password).send_keys(password)
        self.browser.find_element(By.ID, "login-button").click()
        
    def verify_invalid_login(self):
        error_message = self.browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Sorry, this user has been locked out.",error_message



