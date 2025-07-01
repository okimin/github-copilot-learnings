import pytest
from bank_account import BankAccount

def test_deposit_increases_balance():
    acct = BankAccount("Alice", 100)
    acct.deposit(50)
    assert acct.balance() == 150

def test_withdraw_decreases_balance():
    acct = BankAccount("Bob", 200)
    amt = acct.withdraw(80)
    assert amt == 80
    assert acct.balance() == 120

def test_deposit_negative_raises():
    acct = BankAccount("Carol")
    with pytest.raises(ValueError, match="Deposit must be positive"):
        acct.deposit(-10)

def test_withdraw_negative_raises():
    acct = BankAccount("Dan", 50)
    with pytest.raises(ValueError, match="Withdraw must be positive"):
        acct.withdraw(0)

def test_withdraw_insufficient_funds_raises():
    acct = BankAccount("Eve", 30)
    with pytest.raises(ValueError, match="Insufficient funds"):
        acct.withdraw(100)

def test_initial_balance_and_owner():
    acct = BankAccount("Frank")
    assert acct.balance() == 0
    assert acct._owner == "Frank"