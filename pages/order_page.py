import allure

from locators.order_page_locators import OrderPageLocators as loc
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Получаем заголовок окна заказа")
    def get_order_title(self):
        return self.get_text_content(loc.ORDER_HEADER_TITLE)

    @allure.step("Получаем значение таймера")
    def get_order_timer(self):
        return self.get_text_content(loc.ORDER_HEADER_TIME)

    @allure.step("Получаем номер автомобиля")
    def get_car_number(self):
        return self.get_text_content(loc.ORDER_NUMBER)

    @allure.step("Получаем рейтинг водителя")
    def get_driver_rating(self):
        return self.get_text_content(loc.DRIVER_RATING)

    @allure.step("Раскрываем детали поездки")
    def click_details(self):
        self.wait_clickable(loc.DETAILS_BUTTON).click()

    @allure.step("Получаем значение из деталей поездки: {label}")
    def get_details_value(self, label):
        return self.get_text(self.format_locator(loc.DETAILS_ROW_VALUE, label))

    @allure.step("Получаем стоимость поездки из деталей")
    def get_order_cost(self):
        value = self.get_details_value("Еще про поездку")
        return "".join(ch for ch in value if ch.isdigit())

    @allure.step("Нажимаем кнопку «Отменить»")
    def click_cancel(self):
        self.wait_clickable(loc.CANCEL_BUTTON).click()

    @allure.step("Проверяем, что окно заказа отображается")
    def is_order_shown(self):
        return self.is_element_displayed(loc.ORDER_SHOWN)

    @allure.step("Дожидаемся появления окна «Поиск машины»")
    def wait_for_search_started(self, timeout=15):
        self.wait_text_equals(loc.ORDER_HEADER_TITLE, "Поиск машины", timeout)

    @allure.step("Дожидаемся окончания поиска машины")
    def wait_for_driver_arrival(self, timeout=40):
        self.wait_text_contains(loc.ORDER_HEADER_TITLE, "приедет", timeout)
