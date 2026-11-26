import allure


class TestTaxiPreparation:

    @allure.title("Переключение Оптимальный/Быстрый пересчитывает маршрут")
    def test_mode_switch_recalculates(self, main_page):
        main_page.enter_default_route()

        initial_text = main_page.get_results_text()
        initial_duration = main_page.get_results_duration()

        main_page.click_mode("Оптимальный")
        main_page.wait_results_text_changed(initial_text)

        assert main_page.get_active_mode() == "Оптимальный"
        assert main_page.get_results_text() != initial_text
        assert main_page.get_results_duration() != initial_duration

    @allure.title("Вид «Свой» активирует все типы передвижения")
    def test_custom_mode_activates_types(self, main_page):
        main_page.enter_default_route()
        main_page.click_mode("Свой")

        assert main_page.get_active_mode() == "Свой"
        assert main_page.count_disabled_types() == 0

    @allure.title("Вид «Быстрый» активирует кнопку «Вызвать такси»")
    def test_fast_mode_taxi_button_active(self, main_page):
        main_page.enter_default_route()
        main_page.click_mode("Быстрый")

        assert main_page.get_action_button_text() == "Вызвать такси"

    @allure.title("Вид «Свой» и тип «Драйв» активируют кнопку «Забронировать»")
    def test_custom_drive_booking_button_active(self, main_page):
        main_page.enter_default_route()
        main_page.click_mode("Свой")
        main_page.click_type("drive")

        assert main_page.wait_action_button_text("Забронировать") == "Забронировать"
