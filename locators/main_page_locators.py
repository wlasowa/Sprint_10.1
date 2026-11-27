from selenium.webdriver.common.by import By


class MainPageLocators:

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")

    MODE = (By.XPATH, "//div[contains(@class, 'mode') and normalize-space()='{}']")
    ACTIVE_MODE = (By.CSS_SELECTOR, ".mode.active")

    TYPE_BY_ICON = (
        By.XPATH,
        (
            "//div[contains(@class, 'types-container')]"
            "//div[contains(@class, 'type')][.//img[contains(@src, '{}')]]"
        ),
    )
    DISABLED_TYPE = (By.CSS_SELECTOR, ".type.disabled")

    RESULTS_TEXT = (By.CSS_SELECTOR, ".results-container .results-text .text")
    RESULTS_DURATION = (By.CSS_SELECTOR, ".results-container .results-text .duration")
    ACTION_BUTTON = (By.CSS_SELECTOR, ".results-text button.button.round")

    TARIFF_CARD = (
        By.XPATH,
        (
            "//div[contains(@class, 'tcard')]"
            "[.//div[contains(@class, 'tcard-title') and normalize-space()='{}']]"
        ),
    )
    TARIFF_TITLES = (By.CSS_SELECTOR, ".tariff-picker .tcard .tcard-title")
    TARIFF_PRICE = (By.CSS_SELECTOR, ".tcard-price")
    ACTIVE_TARIFF_TITLE = (By.CSS_SELECTOR, ".tariff-picker .tcard.active .tcard-title")
    TARIFF_INFO_BUTTON = (
        By.XPATH,
        (
            "//div[contains(@class, 'tcard')]"
            "[.//div[contains(@class, 'tcard-title') and normalize-space()='{}']]"
            "//button[contains(@class, 'tcard-i')]"
        ),
    )
    TOOLTIP_DESCRIPTION = (
        By.CSS_SELECTOR,
        ".__react_component_tooltip.show .i-dPrefix",
    )

    PHONE_FIELD_TEXT = (By.CSS_SELECTOR, ".np-button .np-text")
    PAYMENT_VALUE = (By.CSS_SELECTOR, ".pp-button .pp-value-text")
    COMMENT_FIELD = (By.CSS_SELECTOR, "#comment")
    REQUIREMENTS_HEADER = (By.CSS_SELECTOR, ".reqs-header .reqs-head")
    LAPTOP_SWITCH = (By.CSS_SELECTOR, ".r-type-switch .switch-input")
    SMART_BUTTON = (By.CSS_SELECTOR, ".smart-button")

    MAP_PLACEMARKS = (By.CSS_SELECTOR, "ymaps[class*='placemark-overlay']")
