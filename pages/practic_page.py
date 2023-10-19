from pages.base_page import BasePage
from pages.locators import PracticPageLocators
first_name = "Secret"
last_name = "Best"
email = "qwe@gmail.com"
mobile = 1234567890
current_address = "Новосибирск, пр-т Лавреньтева, 6/1, 605"

class PracticPage(BasePage):
    practic_locators = PracticPageLocators()

    def set_first_name(self):
        self.set_text(self.practic_locators.first_name, first_name)

    def set_last_name(self):
        self.set_text(self.practic_locators.last_name, last_name)

    def set_email(self):
        self.set_text(self.practic_locators.email, email)

    def click_gender_male(self):
        self.click(self.practic_locators.gender_male)

    def set_mobile(self):
        self.set_text(self.practic_locators.mobile, mobile)

    def click_hobbies_music(self):
        self.click(self.practic_locators.hobbies_music)

    def set_current_address(self):
        self.set_text(self.practic_locators.current_address, current_address)

    def click_submit(self):
        self.click(self.practic_locators.submit_btn)



    # def login(self):
    #     self.set_text(self.locators.login_field, "login")
    #     self.set_text(self.locators.password_field, "password")
    #     self.click(self.locators.login_btn)