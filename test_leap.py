from leap import is_leap

# 0.1
def test_2024_is_a_leap_year():
    assert is_leap(2024)


# 0.2
# def test_1900_is_a_leap_year():
#     assert is_leap(1900)
def test_1900_is_not_a_leap_year():
    assert not is_leap(1900)


# 0.3
import pytest
@pytest.mark.parametrize("year, expected", [
(2000, True), # divisible by 400
(1900, False), # divisible by 100 but not by 400
(2024, True), # divisible by 4 but not by 100
(2023, False), # not divisible by 4
(1, False), # smallest valid year, not divisible by 4
(2400, True), # divisible by 400 (another example)
])
def test_is_leap(year, expected):
    assert is_leap(year) == expected


# 0.4
def test_year_zero_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(0)

def test_negative_year_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(-5)


# 0.5
import pytest
from bank import BankAccount, InsufficientFunds

@pytest.fixture
def account():
    return BankAccount("alice", balance=100)

def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150

def test_withdraw_more_than_balance_is_refused(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(500)
    assert account.balance == 100

def test_each_test_gets_a_fresh_account(account):
    assert account.balance == 100

def test_deposit_zero_is_refused(account):
    with pytest.raises(ValueError):
        account.deposit(0)

def test_withdraw_whole_balance(account):
    account.withdraw(100)
    assert account.balance == 0

def test_two_withdrawals_in_a_row(account):
    account.withdraw(30)
    account.withdraw(20)
    assert account.balance == 50