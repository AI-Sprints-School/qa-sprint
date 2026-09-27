MAX_AMOUNT = 100000        # максимальная сумма одной операции, рублей
FEE_PERCENT = 0.015        # комиссия 1,5%
MIN_FEE = 10.00            # минимальная комиссия, рублей


def format_amount(amount):
    """Сумма строкой с двумя знаками после запятой."""
    return f"{amount:.2f}"


def validate_amount(amount):
    """True, если сумма допустима для операции."""
    return amount > 0 and amount < MAX_AMOUNT


def calculate_fee(amount):
    """Комиссия 1,5% от суммы, округлённая до копеек, но не меньше 10.00."""
    fee = round(amount * FEE_PERCENT)
    if fee < MIN_FEE:
        fee = MIN_FEE
    return fee
