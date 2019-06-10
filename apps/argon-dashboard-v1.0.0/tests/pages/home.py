from tests.pages.components.page import Page
from tests.config.locators import locator


class Home(Page):
    def chart_sales(self):
        return self.find(locator.chart_sales)

    def chart_orders(self):
        return self.find(locator.chart_orders)

    def page_visits_table(self):
        return self.find(locator.page_visits_table)

    def social_traffic_table(self):
        return self.find(locator.social_traffic_table)


