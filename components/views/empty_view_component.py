from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.icon import Icon
from elements.text import Text
import allure

class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-empty-view-icon', 'Icon')
        self.title = Text(page, f'{identifier}t-empty-view-title-text', 'Text')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'Text')

    @allure.step("Check visible empty view '{title}'")
    def check_visible(self, title: str, description: str):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(description)