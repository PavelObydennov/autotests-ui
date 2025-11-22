from components.base_component import BaseComponent
from playwright.sync_api import expect, Page

from elements.input import Input
from elements.text import Text


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page,'login-form-email-input', 'Email' )
        self.password_input = Input(page,'login-form-password-input', 'Password' )
        self.wrong_email_or_password_alert = Text(page,'login-page-wrong-email-or-password-alert', 'Wrong email or password')


    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def check_visible(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')