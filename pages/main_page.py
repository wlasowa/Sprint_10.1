import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import data
from locators import main_page_locators as loc
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Вводим адрес «Откуда»: {address}")
    def enter_from(self, address):
        self.find_element(loc.FROM_FIELD).send_keys(address)

    @allure.step("Вводим адрес «Куда»: {address}")
    def enter_to(self, address):
        field = self.find_element(loc.TO_FIELD)
        field.send_keys(address)
        field.send_keys(Keys.ENTER)

    @allure.step("Строим маршрут: {from_address} → {to_address}")
    def enter_route(self, from_address, to_address):
        self.enter_from(from_address)
        self.enter_to(to_address)

    @allure.step("Строим маршрут по умолчанию")
    def enter_default_route(self):
        self.enter_route(data.FROM_ADDRESS, data.TO_ADDRESS)
        return self

    @allure.step("Строим маршрут с одинаковыми адресами")
    def enter_same_address_route(self):
        self.enter_route(data.FROM_ADDRESS, data.FROM_ADDRESS)
        return self

    @allure.step("Открываем форму заказа такси")
    def open_taxi_form(self):
        self.enter_default_route()
        self.click_mode("Быстрый")
        self.click_action_button()
        return self

    @allure.step("Выбираем вид маршрута «{mode}»")
    def click_mode(self, mode):
        self.wait_clickable(self.format_locator(loc.MODE, mode)).click()

    @allure.step("Получаем активный вид маршрута")
    def get_active_mode(self):
        return self.get_text(loc.ACTIVE_MODE)

    @allure.step("Выбираем тип передвижения «{icon}»")
    def click_type(self, icon):
        self.wait_clickable(self.format_locator(loc.TYPE_BY_ICON, icon)).click()

    @allure.step("Получаем количество заблокированных типов передвижения")
    def count_disabled_types(self):
        return len(self.find_elements(loc.DISABLED_TYPE))

    @allure.step("Получаем текст результата маршрута")
    def get_results_text(self):
        return self.get_text(loc.RESULTS_TEXT)

    @allure.step("Получаем время в пути")
    def get_results_duration(self):
        return self.get_text(loc.RESULTS_DURATION)

    @allure.step("Получаем текст кнопки действия над маршрутом")
    def get_action_button_text(self):
        return self.get_text(loc.ACTION_BUTTON)

    @allure.step("Кликаем по кнопке действия над маршрутом")
    def click_action_button(self):
        self.wait_clickable(loc.ACTION_BUTTON).click()

    @allure.step("Получаем названия тарифов")
    def get_tariff_names(self):
        return [e.get_attribute("innerText").strip() for e in self.find_elements(loc.TARIFF_TITLES)]

    @allure.step("Получаем название активного тарифа")
    def get_active_tariff_name(self):
        return self.get_text(loc.ACTIVE_TARIFF_TITLE)

    @allure.step("Получаем стоимость тарифа «{name}»")
    def get_tariff_cost(self, name):
        card = self.wait_present(self.format_locator(loc.TARIFF_CARD, name))
        price = card.find_element(*loc.TARIFF_PRICE).get_attribute("innerText").strip()
        return "".join(ch for ch in price if ch.isdigit())

    @allure.step("Наводим курсор на иконку «i» тарифа «{name}»")
    def hover_tariff_info(self, name):
        self.wait_clickable(self.format_locator(loc.TARIFF_CARD, name)).click()
        self.hover(self.format_locator(loc.TARIFF_INFO_BUTTON, name))

    @allure.step("Дожидаемся появления кнопки «{text}»")
    def wait_action_button_text(self, text, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: text
            in d.find_element(*loc.ACTION_BUTTON).get_attribute("innerText")
        )
        return self.get_action_button_text()

    @allure.step("Дожидаемся пересчёта результата маршрута")
    def wait_results_text_changed(self, previous_text, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*loc.RESULTS_TEXT).get_attribute("innerText")
            != previous_text
        )

    @allure.step("Получаем описание тарифа из всплывающего окна")
    def get_tooltip_description(self):
        return self.get_text_content(loc.TOOLTIP_DESCRIPTION)

    @allure.step("Получаем текст поля «Телефон»")
    def get_phone_field_text(self):
        return self.get_text(loc.PHONE_FIELD_TEXT)

    @allure.step("Получаем выбранный способ оплаты")
    def get_payment_value(self):
        return self.get_text(loc.PAYMENT_VALUE)

    @allure.step("Проверяем наличие поля «Комментарий водителю»")
    def is_comment_field_displayed(self):
        return self.is_element_displayed(loc.COMMENT_FIELD)

    @allure.step("Получаем заголовок блока требований")
    def get_requirements_header(self):
        return self.get_text(loc.REQUIREMENTS_HEADER)

    @allure.step("Переключаем чекбокс «Столик для ноутбука»")
    def toggle_laptop_table(self):
        self.click_js(loc.LAPTOP_SWITCH)

    @allure.step("Нажимаем кнопку «Ввести номер и заказать»")
    def click_smart_button(self):
        self.wait_clickable(loc.SMART_BUTTON).click()

    @allure.step("Дожидаемся появления {expected} точек на карте")
    def wait_for_placemarks(self, expected, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.find_elements(*loc.MAP_PLACEMARKS)) >= expected
        )
        return len(self.find_elements(loc.MAP_PLACEMARKS))
