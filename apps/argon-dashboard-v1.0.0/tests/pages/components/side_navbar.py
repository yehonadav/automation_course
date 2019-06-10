from qaviton.page import Page
from tests.config.locators import locator


class SideNavbar(Page):
    def components(self):
        return self.find(locator.sidenavbar_components)

    def dashboard(self):
        return self.find(locator.sidenavbar_dashboard)

    def foundation(self):
        return self.find(locator.sidenavbar_foundation)

    def getting_started(self):
        return self.find(locator.sidenavbar_getting_started)

    def icons(self):
        return self.find(locator.sidenavbar_icons)

    def login(self):
        return self.find(locator.sidenavbar_login)

    def maps(self):
        return self.find(locator.sidenavbar_maps)

    def logo(self):
        return self.find(locator.sidenavbar_logo)

    def register(self):
        return self.find(locator.sidenavbar_register)

    def tables(self):
        return self.find(locator.sidenavbar_tables)

    def user_profile(self):
        return self.find(locator.sidenavbar_user_profile)
