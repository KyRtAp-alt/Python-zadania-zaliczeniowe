class InvalidAmountError(Exception):
    pass

class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("The deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("The withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for the withdrawal.")
        self.balance -= amount
    
    def get_balance(self):
        return self.balance