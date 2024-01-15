from selenium import webdriver

class Common:
    def open_browser(self):
        self.browser = webdriver.Chrome()
        url = "https://www.saucedemo.com/"
        self.browser.get(url)
        assert self.browser.current_url == url
        return self.browser
    

    def close_browser(self):
        self.browser.close()