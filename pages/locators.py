from selenium.webdriver.common.by import By    

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    
class BasketPageLocators():
    BASKET_FORMSET = (By.ID, 'basket_formset')
    EMPTY_BASKET_TEXT = (By.ID, 'content_inner')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTR_FORM = (By.ID, 'register_form')
    EMAIL_ADDRESS_FIELD = (By.ID, 'id_registration-email')
    PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD_FIELD = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET_BUTTON = (By.ID, 'add_to_basket_form')
    BOOK_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success.fade.in')
    BOOK_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    BOOK_IN_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    BOOK_PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')