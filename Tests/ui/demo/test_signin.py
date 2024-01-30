import pytest

from Business_Functions.ui.demo.common import Common
from Business_Functions.ui.demo.signin import Signin_page
class Test_signin:
    def setup_method(self):
        self.common = Common()
        self.browser = self.common.open_browser()

    # @after_test
    def teardown_method(self):
        self.common.close_browser()

    def test_signin(self):
        signinpage = Signin_page(self.browser)
        signinpage.signin("Abi","123466")
       
    
    



