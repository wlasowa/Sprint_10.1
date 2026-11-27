from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def format_locator(locator, *args):
        by, value = locator
        return by, value.format(*args)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_clickable(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.TIMEOUT).until(
            ec.element_to_be_clickable(locator)
        )

    def wait_visible(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.TIMEOUT).until(
            ec.visibility_of_element_located(locator)
        )

    def wait_present(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.TIMEOUT).until(
            ec.presence_of_element_located(locator)
        )

    def wait_text_equals(self, locator, text, timeout=None):
        WebDriverWait(self.driver, timeout or self.TIMEOUT).until(
            lambda d: d.find_element(*locator).get_attribute("innerText").strip()
            == text
        )

    def wait_text_contains(self, locator, text, timeout=None):
        WebDriverWait(self.driver, timeout or self.TIMEOUT).until(
            lambda d: text in d.find_element(*locator).get_attribute("innerText")
        )

    def wait_text_changed(self, locator, previous_text, timeout=None):
        WebDriverWait(self.driver, timeout or self.TIMEOUT).until(
            lambda d: d.find_element(*locator).get_attribute("innerText")
            != previous_text
        )

    def wait_count_at_least(self, locator, count, timeout=None):
        WebDriverWait(self.driver, timeout or self.TIMEOUT).until(
            lambda d: len(d.find_elements(*locator)) >= count
        )

    def is_element_displayed(self, locator):
        elements = self.driver.find_elements(*locator)
        return bool(elements) and elements[0].is_displayed()

    def get_text(self, locator):
        return self.wait_visible(locator).get_attribute("innerText").strip()

    def get_text_content(self, locator):
        return self.wait_present(locator).get_attribute("textContent").strip()

    def hover(self, locator):
        element = self.wait_clickable(locator)
        body = self.driver.find_element(By.TAG_NAME, "body")
        ActionChains(self.driver).move_to_element_with_offset(body, 0, 0).perform()
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def click_js(self, locator):
        element = self.wait_present(locator)
        self.driver.execute_script("arguments[0].click();", element)
