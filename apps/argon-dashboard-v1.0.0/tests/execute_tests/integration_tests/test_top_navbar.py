from qaviton.utils.random_util import create_random
from tests.config.supported_platforms import web_app


def test_dashboard_top_navbar(app):
    app.navigate(app.home)
    top_navbar = app.home.top_navbar

    assert top_navbar.brand().text == 'Dashboard'

    random_length = create_random.number(1, 50)
    random_keys = create_random.all_characters(random_length)
    search = top_navbar.search().send(random_keys)
    search.clear()
    try:
        top_navbar.user_dropdown().click()
        assert top_navbar.dropdown_header().text == 'Welcome!'
        top_navbar.dropdown_profile().click()
        app.wait_until_page_loads()
        assert top_navbar.brand().text == 'User profile'

        top_navbar.user_dropdown().click()
        top_navbar.dropdown_settings().click()
        app.wait_until_page_loads()
        assert top_navbar.brand().text == 'User profile'

        top_navbar.user_dropdown().click()
        top_navbar.dropdown_activity().click()
        app.wait_until_page_loads()
        assert top_navbar.brand().text == 'User profile'

        top_navbar.user_dropdown().click()
        top_navbar.dropdown_support().click()
        app.wait_until_page_loads()
        assert top_navbar.brand().text == 'User profile'

        top_navbar.user_dropdown().click()
        top_navbar.dropdown_logout().click()
        app.wait_until_page_loads()
    finally:
        app.driver.get(web_app)
        app.wait_until_page_loads()
