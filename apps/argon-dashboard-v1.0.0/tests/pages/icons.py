from tests.pages.components.page import Page
from tests.config.locators import locator


class Icons(Page):
    def icons(self):
        return self.find_all(locator.icons)
