from selenium import webdriver

class Common:
    def open_browser(self):
        self.browser = webdriver.Chrome() 
        url = "https://demo.automationtesting.in/Index.html"
        self.browser.get(url)
        assert self.browser.current_url == url
        return self.browser
    

    def close_browser(self):
        self.browser.close()