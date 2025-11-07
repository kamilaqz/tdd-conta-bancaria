from bank.account import Account


def test_create_account_with_zero_balance():
    # Cria a conta com saldo inicial de 0
    account = Account()
    assert account.balance == 0
