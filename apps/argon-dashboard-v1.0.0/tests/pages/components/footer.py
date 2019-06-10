from qaviton.page import Page
from tests.config.locators import locator


class Footer(Page):
    def about_us(self):
        return self.find(locator.footer_about_us)

    def blog(self):
        return self.find(locator.footer_blog)

    def copyright(self):
        return self.find(locator.footer_copyright)

    def creative_tim_copyright_link(self):
        return self.find_all(locator.footer_creative_tim_link)[0]

    def creative_tim_link(self):
        return self.find_all(locator.footer_creative_tim_link)[1]
