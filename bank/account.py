class Account:
    def __init__(self) -> None:
        self.balance: float = 0
    
    def deposit(self, amount):
        self.balance += amount
