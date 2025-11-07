from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим кнопку регистрации и проверяем что она задизейблена
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Находим поле email и заполняем его
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    # Находим поле username и заполняем его через клавиатуру
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.focus()

    for i in 'username':
        page.keyboard.type(i, delay=300)

    # Находим поле password и заполняем его
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Проверяем что кнопка стала активной после заполнения полей
    expect(registration_button).to_be_enabled()

    page.wait_for_timeout(3000)