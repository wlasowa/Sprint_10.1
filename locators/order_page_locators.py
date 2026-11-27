from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_SHOWN = (By.CSS_SELECTOR, ".order.shown")
    ORDER_HEADER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
    ORDER_HEADER_TIME = (By.CSS_SELECTOR, ".order-header-time")
    ORDER_NUMBER = (By.CSS_SELECTOR, ".order-number .number")
    DRIVER_RATING = (By.CSS_SELECTOR, ".order-btn-rating")
    CANCEL_BUTTON = (
        By.XPATH,
        (
            "//div[contains(@class, 'order-btn-group')]"
            "[.//div[normalize-space()='Отменить']]//button"
        ),
    )
    DETAILS_BUTTON = (
        By.XPATH,
        (
            "//div[contains(@class, 'order-btn-group')]"
            "[.//div[normalize-space()='Детали']]//button"
        ),
    )
    DETAILS_ROW_VALUE = (
        By.XPATH,
        (
            "//div[contains(@class, 'order-details-row')]"
            "[.//div[contains(@class, 'o-d-h') and normalize-space()='{}']]"
            "//div[contains(@class, 'o-d-sh')]"
        ),
    )
