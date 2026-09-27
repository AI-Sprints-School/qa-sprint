from wallet import Wallet, calculate_fee


def test_deposit_increases_balance():
    wallet = Wallet(100)
    wallet.deposit(50)
    assert wallet.balance == 150


def test_balance_after_deposit():
    wallet = Wallet(100)
    wallet.deposit(50)
    expected = wallet.balance
    assert wallet.balance == expected


def test_withdraw_works():
    wallet = Wallet(100)
    wallet.withdraw(30)
    assert wallet is not None


def test_withdraw_more_than_balance_keeps_balance():
    wallet = Wallet(100)
    wallet.withdraw(150)
    assert wallet.balance == 100


def test_withdraw_updates_history():
    wallet = Wallet(100)
    wallet.withdraw(30)
    assert wallet._last_operation == "withdraw:30"


def test_fee_is_correct():
    result = calculate_fee(1000)
    assert result == calculate_fee(1000)
