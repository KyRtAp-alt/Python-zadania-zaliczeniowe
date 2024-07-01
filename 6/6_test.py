import pytest
from z6 import BankAccount, InvalidAmountError, InsufficientFundsError

def test_initial_balance():
    account = BankAccount()
    assert account.get_balance() == 0
    
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount()
    
    account.deposit(50)
    assert account.get_balance() == 50
    
    account.deposit(100)
    assert account.get_balance() == 150

def test_deposit_invalid_amount():
    account = BankAccount()
    
    with pytest.raises(InvalidAmountError):
        account.deposit(0)
        
    with pytest.raises(InvalidAmountError):
        account.deposit(-10)

def test_withdraw():
    account = BankAccount(200)
    
    account.withdraw(50)
    assert account.get_balance() == 150
    
    account.withdraw(100)
    assert account.get_balance() == 50

def test_withdraw_invalid_amount():
    account = BankAccount(200)
    
    with pytest.raises(InvalidAmountError):
        account.withdraw(0)
        
    with pytest.raises(InvalidAmountError):
        account.withdraw(-10)

def test_withdraw_insufficient_funds():
    account = BankAccount(50)
    
    with pytest.raises(InsufficientFundsError):
        account.withdraw(100)

def test_get_balance():
    account = BankAccount(300)
    assert account.get_balance() == 300

    account.deposit(100)
    assert account.get_balance() == 400
    
    account.withdraw(50)
    assert account.get_balance() == 350