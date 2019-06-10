from qaviton.locator import Locator


class locator(Locator):
    sidenavbar_logo            = ('src', './assets/img/brand/blue.png')
    sidenavbar_dashboard       = ('xpath', '//*[@id="sidenav-collapse-main"]//*[@href="./index.html"]')
    sidenavbar_icons           = ('href', './examples/icons.html')
    sidenavbar_maps            = ('href', './examples/maps.html')
    sidenavbar_user_profile    = ('xpath', '//*[@id="sidenav-collapse-main"]//*[@href="./examples/profile.html"]')
    sidenavbar_tables          = ('href', './examples/tables.html')
    sidenavbar_login           = ('href', './examples/login.html')
    sidenavbar_register        = ('href', './examples/register.html')
    sidenavbar_getting_started = ('href', 'https://demos.creative-tim.com/argon-dashboard/docs/getting-started/overview.html')
    sidenavbar_foundation      = ('href', 'https://demos.creative-tim.com/argon-dashboard/docs/foundation/colors.html')
    sidenavbar_components      = ('href', 'https://demos.creative-tim.com/argon-dashboard/docs/components/alerts.html')

    topnavbar_brand = ('src', './assets/img/brand/blue.png')
    topnavbar_search = ('xpath', '//*[@id="navbar-main"]//input[@type="text"]')
    topnavbar_user_dropdown = ('xpath', '//*[@id="navbar-main"]//a[@role="button"]')
    topnavbar_dropdown_header = ('xpath', '//*[@id="navbar-main"]//*[text()="Welcome"]')
    topnavbar_dropdown_profile = ('xpath', '//*[@id="navbar-main"]//*[text()="My profile"]')
    topnavbar_dropdown_settings = ('xpath', '//*[@id="navbar-main"]//*[text()="Settings"]')
    topnavbar_dropdown_activity = ('xpath', '//*[@id="navbar-main"]//*[text()="Activity"]')
    topnavbar_dropdown_support = ('xpath', '//*[@id="navbar-main"]//*[text()="Support"]')
    topnavbar_dropdown_logout = ('xpath', '//*[@id="navbar-main"]//*[text()="Logout"]')

    footer_copyright = ('class name', 'copyright')
    footer_creative_tim_link = ('xpath', '//footer//*[@href="https://www.creative-tim.com"]')  # will return 2 elements
    footer_about_us = ('xpath', '//footer//*[@href="https://www.creative-tim.com/presentation"]')
    footer_blog = ('xpath', '//footer//*[@href="http://blog.creative-tim.com"]')
    footer_license = ('xpath', '//footer//*[@href="https://github.com/creativetimofficial/argon-dashboard/blob/master/LICENSE.md"]')

    icons = ('xpath', '//*[@class="row icon-examples"]//button')
    map = ('id', 'map-canvas')

    profile_input_username = ('id', 'input-username')
    profile_input_firstname = ('id', 'input-first-name')
    profile_input_email = ('id', 'input-email')
    profile_input_lastname = ('id', 'input-last-name')
    profile_input_address = ('id', 'input-address')
    profile_input_city = ('id', 'input-city')
    profile_input_country = ('id', 'input-country')
    profile_input_postalcode = ('id', 'input-postal-code')
    profile_about_me = ('tag name', 'textarea')
    profile_friends = ('xpath', '//*[text()="Friends"]/parent::*/span[@class="heading"]')
    profile_photos = ('xpath', '//*[text()="Photos"]/parent::*/span[@class="heading"]')
    profile_comments = ('xpath', '//*[text()="Comments"]/parent::*/span[@class="heading"]')
    profile_card = ('class name', 'card-profile')

    tables = ('tag name', 'table')

    github_button = ('text', 'Github')
    google_button = ('text', 'Google')
    name_field = ('type', 'text')
    email_field = ('type', 'email')
    password_field = ('type', 'password')
    checkbox_button = ('type', 'checkbox')
    submit_button = ('type', 'button')

    chart_sales = ('id', 'chart-sales')
    chart_orders = ('id', "chart-orders")
    page_visits_table = ('text', 'Page visits')
    social_traffic_table = ('text', 'Social traffic')
