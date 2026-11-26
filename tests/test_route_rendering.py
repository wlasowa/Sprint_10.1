import allure
import pytest

import data

ADDRESS_PAIRS = [
    (data.FROM_ADDRESS, data.TO_ADDRESS),
    (data.TO_ADDRESS, data.FROM_ADDRESS),
]


class TestRouteRendering:

    @allure.title("Отрисовка двух точек на карте при вводе разных адресов")
    @pytest.mark.parametrize(
        "from_address, to_address",
        ADDRESS_PAIRS,
        ids=["direct", "reverse"],
    )
    def test_two_placemarks_on_map(self, main_page, from_address, to_address):
        main_page.enter_route(from_address, to_address)
        assert main_page.wait_for_placemarks(2) == 2
