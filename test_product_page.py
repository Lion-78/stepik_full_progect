import pytest
import time

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

regist_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
product_link_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

urls = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail(reason="bugged")
    ),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
]

@pytest.mark.regloguser
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, regist_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = '1Cjkysirj1-'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser): 
        page = ProductPage(browser, product_link_page)
        product_page = ProductPage(browser, browser.current_url)
        product_page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link_page)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_to_basket()
        product_page.success_message_should_contain_book_name()
        product_page.price_in_basket_should_be_book_price()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link_page)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link_page)
    page.open()
    page.go_to_login_page()
    
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()
    product_page.success_message_should_contain_book_name()
    product_page.price_in_basket_should_be_book_price()
    
@pytest.mark.xfail(reason='chek')    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, product_link_page)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser): 
    page = ProductPage(browser, product_link_page)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message()
    
@pytest.mark.xfail(reason='chek')
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, product_link_page)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_basket()
    product_page.should_be_disappeared()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_link_page)
    page.open()
    page.open_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.expect_basket_is_empty()
    page.expext_message_basket_is_empty()