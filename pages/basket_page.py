from .base_page import BasePage
from .locators import BasketPageLocators

import time

class BasketPage(BasePage):
    def expect_basket_is_empty(self):
        # Ожидаем, что в корзине нет товаров
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), "Basket is not empty!"
        
        # Ожидаем, что есть текст о том что корзина пуста 
    def expext_message_basket_is_empty(self):
        text_empty = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert 'Your basket is empty.' in text_empty