import time
from pages.practic_page import PracticPage, first_name, email
from pages.student_page import StudentPage

class TestForma:
    # вводим данные в полях и кликаем радиобаттоны
    def test_open(self, setup):
        page = PracticPage(setup)
        page.open_url(" https://demoqa.com/automation-practice-form")
        page.set_first_name()
        page.set_last_name()
        page.set_email()
        page.click_gender_male()
        page.set_mobile()
        page.click_hobbies_music()
        page.set_current_address()
        time.sleep(5)
        page.click_submit()
        time.sleep(5)

    def test_student_name(self, setup):
        student = StudentPage(setup)
        student_name = student.get_student_name()
        assert first_name in student_name




