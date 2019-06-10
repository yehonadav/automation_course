def test_dashboard_elements_exist(app):
    app.navigate(app.home)

    app.home.social_traffic_table()
    app.home.page_visits_table()
    app.home.chart_orders()
    app.home.chart_sales()
