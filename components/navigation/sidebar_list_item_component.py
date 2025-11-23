from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, title: str):
        super().__init__(page)

        self.identifier = identifier
        self.expected_title = title

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', '')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', title)
        self.button = Button(page, f'{identifier}-drawer-list-item-button', title)

    def check_visible(self):
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(self.expected_title)
        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)