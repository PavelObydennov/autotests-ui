from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Открываем страницу
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Находим поле email и заполняем
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        # Находим поле username и заполняем
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        # Находим поле password и заполняем
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        # Находим кнопку регистрации
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохраняем состояние браузера
        context.storage_state(path="browser-state.json")


    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Находим локатор заголовка "Courses" и проверяем
        courses_locator = page.locator(
            "//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1 css-q94ntb']//h6")
        expect(courses_locator).to_be_visible()
        expect(courses_locator).to_have_text('Courses')

        # Находим локатор блока "There is no results" и проверяем
        courses_locator = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_locator).to_be_visible()
        expect(courses_locator).to_have_text('There is no results')

        # Находим локатор иконки и проверяем
        courses_locator = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_locator).to_be_visible()
        expect(courses_locator).to_be_attached()

        # Находим локатор блока: "Results from the load test pipeline will be displayed here" и проверяем
        courses_locator = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_locator).to_be_visible()
        expect(courses_locator).to_have_text('Results from the load test pipeline will be displayed here')