from wallet import Wallet, calculate_fee


def test_withdraw_decreases_balance():
    wallet = Wallet(100)
    wallet.withdraw(30)
    assert wallet.balance == 70
