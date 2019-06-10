from qaviton import crosstest
from tests.config.secret import hub


web_app = 'https://demos.creative-tim.com/argon-dashboard/index.html'


screenResolution = "800x600x24"
sessionTimeout = 60


# create cross-platform testing object
platforms = crosstest.Platforms()
platforms.web.command_executor = hub


# add chrome browser support
platforms.web({
    'browserName': "chrome",
    'version': "",
    'platform': "ANY",
    'app': web_app,
    'screenResolution': screenResolution,
    'sessionTimeout': sessionTimeout,
    'enableVNC': True,
    'enableVideo': True,
    'name': "{}",
    'videoName': "{}.mp4",
    'logName': "{}.log"})
