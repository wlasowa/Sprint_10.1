import allure
import pytest

import data

TAXI_TARIFF_CASES = []

for name, description in data.TAXI_TARIFFS:
    marks = []
    if name in data.BUGGY_TARIFFS:
        marks.append(
            pytest.mark.xfail(
                reason="Описание тарифа в подсказке не соответствует ТЗ"
            )
        )
    TAXI_TARIFF_CASES.append(
        pytest.param(name, description, id=data.TARIFF_IDS[name], marks=marks)
    )


class TestTaxiOrder:

    @allure.title("Форма заказа такси отображает шесть тарифов с одним активным")
    def test_taxi_form_has_six_tariffs_one_active(self, main_page):
        main_page.open_taxi_form()

        assert main_page.get_tariff_names() == data.TAXI_TARIFF_NAMES
        assert main_page.get_active_tariff_name() == "Рабочий"

    @allure.title("Подсказка тарифа «{name}» соответствует описанию из ТЗ")
    @pytest.mark.parametrize("name, description", TAXI_TARIFF_CASES)
    def test_tariff_tooltip_matches_tz(self, main_page, name, description):
        main_page.open_taxi_form()
        main_page.hover_tariff_info(name)

        assert main_page.get_tooltip_description() == description

    @allure.title("Форма заказа такси содержит поля Телефон, Способ оплаты, Комментарий, Требования")
    def test_taxi_form_fields_present(self, main_page):
        main_page.open_taxi_form()

        assert main_page.get_phone_field_text() == "Телефон"
        assert main_page.get_payment_value() == "Наличные"
        assert main_page.is_comment_field_displayed()
        assert main_page.get_requirements_header() == "Требования к заказу"

    @allure.title("Полный сценарий заказа такси")
    def test_taxi_full_order_flow(self, main_page, order_page):
        main_page.open_taxi_form()
        expected_cost = main_page.get_tariff_cost("Рабочий")

        main_page.toggle_laptop_table()
        main_page.click_smart_button()

        order_page.wait_for_search_started()
        search_title = order_page.get_order_title()
        search_timer = order_page.get_order_timer()

        order_page.wait_for_driver_arrival()
        order_title = order_page.get_order_title()
        car_number = order_page.get_car_number()
        driver_rating = order_page.get_driver_rating()

        order_page.click_details()
        order_cost = order_page.get_order_cost()

        order_page.click_cancel()
        order_shown = order_page.is_order_shown()

        assert search_title == "Поиск машины"
        assert search_timer != ""
        assert "мин." in order_title
        assert car_number != ""
        assert driver_rating != ""
        assert order_cost == expected_cost
        assert not order_shown
