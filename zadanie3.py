import pytest


# REMEMBER TO DELETE "PASS"

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


def test_withdraw_success():
    # your code goes here
    pass


def test_withdraw_negative_amount():
    # your code goes here
    pass


def test_withdraw_insufficient_funds():
    # your code goes here
    pass
