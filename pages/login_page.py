import allure

from pages.base_page import BasePage
from pages.locators import Login_page_locators

class LoginPage(BasePage):


    def user_login(self):
        with allure.step(f"Войти в систему"):

            self.set_text(Login_page_locators.field_login, "sys112")
            self.set_text(Login_page_locators.field_password, "Qwerty1234@@")


