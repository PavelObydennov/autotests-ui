from playwright.sync_api import Page,expect
from components.base_component import BaseComponent
from elements.input import Input
import allure


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_email_input = Input(page,'registration-form-email-input', 'Email')
        self.registration_username_input = Input(page,'registration-form-username-input', 'Username')
        self.registration_password_input = Input(page,'registration-form-password-input', 'Password')

    @allure.step('Fill registration form')
    def fill_registration_form(self, email: str, username: str, password: str):
        self.registration_email_input.fill(email)
        self.registration_email_input.check_have_value(email)

        self.registration_username_input.fill(username)
        self.registration_username_input.check_have_value(username)

        self.registration_password_input.fill(password)
        self.registration_password_input.check_have_value(password)
    @allure.step('Check visible registration form')
    def check_visible(self):
        expect(self.registration_email_input).to_be_visible()
        expect(self.registration_username_input).to_be_visible()
        expect(self.registration_password_input).to_be_visible()


