from tests.pages.components.page import Page
from tests.config.locators import locator


class Tables(Page):
    def github_button(self):
        return self.find(locator.tables)
