from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим и заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    # Находим и заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    # Находим и заполняем поле password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # Находим кнопку registration и нажимаем ее
    button_registration = page.get_by_test_id('registration-page-registration-button')
    button_registration.click()

    # Найдем локатор для Dashboard
    dashboard_locator = page.locator("//*[@data-testid='dashboard-toolbar-title-text']")
    expect(dashboard_locator).to_be_visible()
    expect(dashboard_locator).to_have_text('Dashboard')

    # page.wait_for_timeout(3000) - для отслеживания прохождения