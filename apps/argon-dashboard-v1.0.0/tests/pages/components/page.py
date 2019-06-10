from qaviton.page import Page as page
from tests.pages.components.footer import Footer
from tests.pages.components.side_navbar import SideNavbar
from tests.pages.components.top_navbar import TopNavbar


class Page(page):
    """component with common behavior to all pages & components alike.
    all of your pages & components should inherit from this common page.

    you should always include here a navigation to your initial login page(starting point)
    so that dependent tests could always start fresh if needed.
    """
    def __init__(self, driver, platform):
        page.__init__(self, driver, platform=platform)
        self.top_navbar = TopNavbar(driver, platform=platform)
        self.side_navbar = SideNavbar(driver, platform=platform)
        self.footer = Footer(driver, platform=platform)
