from typing import Pattern
import allure
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Открываем страницу {url}'):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):  # Метод для перезагрузки страницы
        with allure.step(f'Перезагружаем страницу "{self.page.url}"'):
            self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Проверяем, что текущий URL соответствует ожидаемому: {expected_url.pattern}'):
            expect(self.page).to_have_url(expected_url)