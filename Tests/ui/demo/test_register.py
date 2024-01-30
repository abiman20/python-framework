import pytest

from Business_Functions.ui.demo.common import Common
from Business_Functions.ui.demo.register import Register_page


class Test_register:
    def setup_method(self):
        self.common = Common()
        self.browser = self.common.open_browser()

    # @after_test
    def teardown_method(self):
        self.common.close_browser()

    def test_register(self):
        registerpage = Register_page(self.browser)
        registerpage.signuppage("designerfashion1100@gmail.com")
        registerpage.verify_register_page()
        registerpage.register("abi","arasu")
        registerpage.radio_button()
        registerpage.check_box()
        registerpage.drop_down()
      

