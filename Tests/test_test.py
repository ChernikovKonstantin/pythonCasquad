import os
import time

import requests

from pages.practic_page import PracticPage, first_name, email
from pages.student_page import StudentPage
from pages.login_page import LoginPage

class TestForma:
    # открытие страницы, отработка фикстуры
    def test_open_t(self, setup):
        page = PracticPage(setup)
        page.open_url(" https://demoqa.com/automation-practice-form")

    def test_login(self, setup):

        page = PracticPage(setup)
        page.open_url("https://101.test.tanto-s.ru")

        page = LoginPage()
        page.user_login()


    def test_login_api(self, setup):

        page = PracticPage(setup)
        page.open_url(" https://101.test.tanto-s.ru")
        #print(page.get_current_url())

        base_url = page.get_current_url()
        response = requests.get(base_url)
        #

        # return response.json()


    def test_open(self, setup):
        page = PracticPage(setup)
        page.open_url(" https://demoqa.com/automation-practice-form")


    def test_student_name(self, setup):
        student = StudentPage(setup)
        student_name = student.get_student_name()
        assert first_name in student_name




