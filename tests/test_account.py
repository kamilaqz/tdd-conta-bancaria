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


def test_withdraw_decreases_balance():
    # Saca um valor e verifica se o saldo diminui
    account = Account()
    account.deposit(100)
    account.withdraw(30)
    assert account.balance == 70


def test_get_balance_returns_current_balance():
    # Consulta o saldo atual
    account = Account()
    account.deposit(150)
    account.withdraw(50)
    assert account.get_balance() == 100


def test_transfer_between_accounts():
    # Transfere dinheiro entre duas contas
    account1 = Account()
    account2 = Account()
    account1.deposit(100)
    account1.transfer(50, account2)
    assert account1.balance == 50
    assert account2.balance == 50


def test_account_statement():
    # Mostra um extrato com todas as transações
    account = Account()
    account.deposit(100)
    account.withdraw(30)
    account.deposit(50)
    statement = account.get_statement()
    assert len(statement) == 3
    assert statement[0] == "Depósito: +100"
    assert statement[1] == "Saque: -30"
    assert statement[2] == "Depósito: +50"
