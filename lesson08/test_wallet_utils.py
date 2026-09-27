from wallet_utils import format_amount, validate_amount, calculate_fee


def test_format_amount_1000_has_two_decimals():
    # Arrange
    amount = 1000
    # Act
    result = format_amount(amount)
    # Assert
    assert result == "1000.00"


# Ваши тесты пишутся ниже, каждый — отдельной функцией с именем test_*.
# Ожидаемые значения берутся из таблицы в SPEC.md и больше ниоткуда.
