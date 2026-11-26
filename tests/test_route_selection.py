import allure

import data


class TestRouteSelection:

    @allure.title("Отрисовка блока выбора маршрута при разных адресах")
    def test_route_block_appears_for_distinct_addresses(self, main_page):
        main_page.enter_default_route()
        assert "В пути" in main_page.get_results_duration()

    @allure.title("Одинаковый адрес отображает «Авто Бесплатно В пути 0 мин.»")
    def test_same_address_shows_auto_free(self, main_page):
        main_page.enter_same_address_route()
        assert data.SAME_ADDRESS_AUTO_FREE in main_page.get_results_text()
        assert data.SAME_ADDRESS_DURATION in main_page.get_results_duration()
