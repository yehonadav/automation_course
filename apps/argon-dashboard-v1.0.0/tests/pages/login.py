from tests.pages.components.page import Page
from tests.config.locators import locator


class Login(Page):
    def github_button(self):
        return self.find(locator.github_button)

    def google_button(self):
        return self.find(locator.google_button)

    def name_field(self):
        return self.find(locator.name_field)

    def email_field(self):
        return self.find(locator.email_field)

    def checkbox_button(self):
        return self.find(locator.checkbox_button )

    def submit_button(self):
        return self.find(locator.submit_button)
