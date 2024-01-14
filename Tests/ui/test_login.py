# test framework
import pytest

from Business_Functions.ui.common import Common
from Business_Functions.ui.login_page import Login_page
from Business_Functions.ui.product_page import Product_page

class Test_login:

    # @before_test
    def setup_method(self):
        self.common = Common()
        self.browser = self.common.open_browser()

    # @after_test
    def teardown_method(self):
        self.common.close_browser()

    # @Test
    def test_valid_login(self):
        # Given: im on login page
        loginpage = Login_page(self.browser)
        # when: I enter login details
        loginpage.login_saucelab("standard_user","secret_sauce")
        # Then: I validate if login is successful
        productpage = Product_page(self.browser)
        productpage.verify_product_page()

    def test_invalid_login(self):
        # Given : im on login page
        loginpage = Login_page(self.browser)
        # When : I enter login details
        loginpage.login_saucelab("xyz","secret_sauce")
        # Then : I validate whether login is succesfull or not
        loginpage.verify_invalid_login()

    # def test_product_page(self):
    #     self.test_valid_login()

    