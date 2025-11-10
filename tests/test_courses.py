from playwright.sync_api import expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
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