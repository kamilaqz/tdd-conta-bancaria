from bank.account import Account


def test_create_account_with_zero_balance():
    # Cria a conta com saldo inicial de 0
    account = Account()
    assert account.balance == 0


def test_deposit_increases_balance():
    # Deposita um valor e verifica se o saldo aumenta
    account = Account()
    account.deposit(100)
    assert account.balance == 100
