import selectors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Register_page:

    def __init__(self,browser)-> None:
        self.browser: webdriver.Chrome = browser
        
    def signuppage(self,email):
        self.email = "email"
        self.browser.find_element(By.ID, self.email).send_keys(email)
        self.browser.find_element(By.ID,"enterimg").click()
        
    def verify_register_page(self):
        register_page = "https://demo.automationtesting.in/Register.html"
        assert self.browser.current_url == register_page, self.browser.current_url + 'is not equal to' + register_page
        title = self.browser.find_element(By.XPATH,'//h2[text() = "Register"]').text
        assert title == "Register", title
        title = self.browser.find_element(By.XPATH, "//p[text()='Do not consent']").click()


    def register(self,firstname,lastname):
        self.firstname = '//input[@placeholder="First Name"]'
        self.lastname = '//input[@placeholder="Last Name"]'
        self.browser.find_element(By.XPATH,self.firstname ).send_keys(firstname)
        self.browser.find_element(By.XPATH,self.lastname).send_keys(lastname)

    def radio_button(self):
        self.browser.find_element(By.XPATH, '//input[@value="FeMale"]').click()

    def check_box(self):
        list = self.browser.find_elements(By.XPATH,"//input[@type='checkbox']")
        for ele in list:
            val = ele.get_attribute('value')
            if val == 'Movies':
                ele.click()

    def drop_down(self):
        skill = self.browser.find_element(By.ID, "Skills")
        obj = Select(skill)
        obj.select_by_visible_text("Design")







    


    
    
    