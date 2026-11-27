import pytest

import data


def taxi_tariff_cases():
    cases = []
    for name, description in data.TAXI_TARIFFS:
        marks = []
        if name in data.BUGGY_TARIFFS:
            marks.append(
                pytest.mark.xfail(
                    reason="Описание тарифа в подсказке не соответствует ТЗ"
                )
            )
        cases.append(
            pytest.param(name, description, id=data.TARIFF_IDS[name], marks=marks)
        )
    return cases
