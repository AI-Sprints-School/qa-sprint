from wallet_utils import calculate_fee, MAX_AMOUNT, FEE_PERCENT, MIN_FEE


class Wallet:
    """Упрощённая модель кошелька для учебных тестов.

    Комиссия за списание здесь не удерживается: её считает отдельная
    функция calculate_fee. Пополнение по тарифу BASIC бесплатно.
    """

    def __init__(self, balance):
        self.balance = balance
        self._last_operation = None

    def deposit(self, amount):
        """Пополнение: баланс увеличивается на amount."""
        self.balance = self.balance + amount
        self._last_operation = f"deposit:{amount}"

    def withdraw(self, amount):
        """Списание. Если amount больше баланса, баланс не меняется."""
        if amount > self.balance:
            self._last_operation = f"rejected:{amount}"
            return False
        self.balance = self.balance - amount
        self._last_operation = f"withdraw:{amount}"
        return True
