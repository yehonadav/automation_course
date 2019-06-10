import time


def test_health_check(app):
    t = time.time()
    app.navigate(app.home)
    app.wait_until_page_loads(timeout=30)
    page_load = time.time() - t

    assert page_load < 15
