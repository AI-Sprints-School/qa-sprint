from wallet_utils import format_amount, validate_amount, calculate_fee


def test_format_amount_1000_has_two_decimals():
    # Arrange
    amount = 1000
    # Act
    result = format_amount(amount)
    # Assert
    assert result == "1000.00"


# Ниже — тесты заданий 4.2 и 4.4, каждый отдельной функцией с именем test_*.
# Задание 4.2: сначала готовый тест из задания, под ним — ваш на calculate_fee.
# Задание 4.4: ещё один ваш тест — против выжившего мутанта.
# Ожидаемые значения берутся из таблицы в SPEC.md и больше ниоткуда.
