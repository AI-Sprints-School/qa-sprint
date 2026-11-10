"""Заведомо сломанная копия кошелька — служебный файл задания 3.4.

К коду применены три поломки из lesson07/breakages.md: П1, П2 и П3.
По нему проверяющий сверяет эталон матрицы «поломка × тест»: подставить
вместо lesson08/wallet.py и прогнать lesson07/tests_to_review.py.
В работе студента он не используется, читать и править его не нужно.
"""
from wallet_utils import MAX_AMOUNT, FEE_PERCENT, MIN_FEE


def calculate_fee(amount):
    # П3: комиссия всегда ноль
    return 0


class Wallet:
    def __init__(self, balance):
        self.balance = balance
        self._last_operation = None

    def deposit(self, amount):
        # П1: пополнение прибавляет на 10 меньше, чем просили
        self.balance = self.balance + amount - 10
        self._last_operation = f"deposit:{amount}"

    def withdraw(self, amount):
        # П2: списание разрешает уйти в минус и списывает всегда
        self.balance = self.balance - amount
        self._last_operation = f"withdraw:{amount}"
        return True
