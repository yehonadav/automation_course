from qaviton.navigator import Navigator
from tests.pages.components.page import Page
from tests.pages.home import Home
from tests.pages.icons import Icons
from tests.pages.login import Login
from tests.pages.maps import Maps
from tests.pages.profile import Profile
from tests.pages.register import Register
from tests.pages.tables import Tables


class App(Page):
    """use the app page to include all your
    pages/components/api/services/flows
    in a single page application
    """
    def __init__(self, driver, platform):
        Page.__init__(self, driver, platform=platform)
        self.home = Home(driver, platform=platform)
        self.icons = Icons(driver, platform=platform)
        self.login = Login(driver, platform=platform)
        self.maps = Maps(driver, platform=platform)
        self.profile = Profile(driver, platform=platform)
        self.register = Register(driver, platform=platform)
        self.tables = Tables(driver, platform=platform)
        
        self.navigate = Navigator(self.home, auto_connect=self)
