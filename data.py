FROM_ADDRESS = "Хамовнический вал, 34"
TO_ADDRESS = "Зубовский бульвар, 37"

SAME_ADDRESS_AUTO_FREE = "Авто Бесплатно"
SAME_ADDRESS_DURATION = "В пути 0 мин."

ADDRESS_PAIRS = [
    (FROM_ADDRESS, TO_ADDRESS),
    (TO_ADDRESS, FROM_ADDRESS),
]

TAXI_TARIFFS = [
    ("Рабочий", "Для деловых особ, которых отвлекают"),
    ("Сонный", "Для тех, кто не выспался"),
    ("Отпускной", "Если пришла пора отдохнуть"),
    ("Разговорчивый", "Если мысли не выходят из головы"),
    ("Утешительный", "Если хочется свернуться калачиком"),
    ("Глянцевый", "Если нужно блистать"),
]

TAXI_TARIFF_NAMES = [name for name, _ in TAXI_TARIFFS]

BUGGY_TARIFFS = ("Сонный", "Разговорчивый")

TARIFF_IDS = {
    "Рабочий": "working",
    "Сонный": "sleepy",
    "Отпускной": "vacation",
    "Разговорчивый": "talkative",
    "Утешительный": "comforting",
    "Глянцевый": "glossy",
}
