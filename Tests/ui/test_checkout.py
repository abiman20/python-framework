import pytest
from Business_Functions.ui.checkout_page import Checkout_page
from Business_Functions.ui.common import Common
from Business_Functions.ui.login_page import Login_page
from Business_Functions.ui.product_page import Product_page
from Business_Functions.ui.addtocart_page import Cart_page


class Test_checkout:

    def setup_method(self):
        self.common = Common()
        self.browser = self.common.open_browser()

    def teardown_method(self):
        self.common.close_browser()


    def test_product_checkout(self):
        #Given : am logged into saucelab
        loginpage = Login_page(self.browser)
        loginpage.login_saucelab("standard_user","secret_sauce")
        productpage = Product_page(self.browser)
        productpage.verify_product_page()
        #When : i add a product to cart
        product_name,product_description,product_price = productpage.add_product_to_cart()
        productpage.go_to_cart()
        addtocart_page = Cart_page(self.browser)
        addtocart_page.verify_add_to_cart_page(product_name,product_description,product_price)
        #When : i checkout the product
        check_out_page = Checkout_page(self.browser)
        check_out_page.checkout_item()
        check_out_page.verify_checkout_page()
        check_out_page.checkout_information("abi","naga","m40")
        check_out_page.checkout_step_two()
        #Then : product checkout successful


      