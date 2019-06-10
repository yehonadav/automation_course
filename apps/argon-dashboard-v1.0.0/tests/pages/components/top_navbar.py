from qaviton.page import Page
from tests.config.locators import locator


class TopNavbar(Page):
    def brand(self):
        return self.find(locator.topnavbar_brand)

    def dropdown_activity(self):
        return self.find(locator.topnavbar_dropdown_activity)

    def dropdown_header(self):
        return self.find(locator.topnavbar_dropdown_header)

    def dropdown_logout(self):
        return self.find(locator.topnavbar_dropdown_logout)

    def dropdown_profile(self):
        return self.find(locator.topnavbar_dropdown_profile)

    def dropdown_settings(self):
        return self.find(locator.topnavbar_dropdown_settings)

    def dropdown_support(self):
        return self.find(locator.topnavbar_dropdown_support)

    def search(self):
        return self.find(locator.topnavbar_search)

    def user_dropdown(self):
        return self.find(locator.topnavbar_user_dropdown)
