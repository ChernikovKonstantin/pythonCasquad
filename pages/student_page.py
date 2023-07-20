from pages.base_page import BasePage
from pages.locators import StudentPageLocators


class StudentPage(BasePage):
    student_locators = StudentPageLocators()

    def get_student_name(self):
        self.return_text(self.student_locators.student_name)

    def get_student_email(self):
        self.return_text(self.student_locators.student_email)

    def set_email(self):
        self.set_text(self.practic_locators.email, "qwe@gmail.com")

    def click_gender_male(self):
        self.click(self.practic_locators.gender_male)

    def set_mobile(self):
        self.set_text(self.practic_locators.mobile, "1234567890")

    def click_hobbies_music(self):
        self.click(self.practic_locators.hobbies_music)

    def set_current_address(self):
        self.set_text(self.practic_locators.current_address, "Новосибирск, пр-т Лавреньтева")

    def click_submit(self):
        self.click(self.practic_locators.submit_btn)