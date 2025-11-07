class Account:
    def __init__(self) -> None:
        self.balance: float = 0
    
    def deposit(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("O valor deve ser um número")
        if amount <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero")
        self.balance += amount
    
    def withdraw(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("O valor deve ser um número")
        if amount <= 0:
            raise ValueError("O valor do saque deve ser maior que zero")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente")
        self.balance -= amount
