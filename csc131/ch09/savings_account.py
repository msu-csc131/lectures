"""
File: savings_account.py
This module defines the SavingsAccount class.
"""


class SavingsAccount:
    """This class represents a savings account with the owner's name, PIN, and balance."""

    RATE = 0.02  # Single rate for all accounts (class variable)

    def __init__(self, name: str, pin: str, balance: float = 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance

    def __str__(self) -> str:
        """
        Returns the string rep.
        :return A string representation of this SavingsAccount is returned.
        """
        result = 'Name:    ' + self._name + '\n'
        result += 'PIN:     ' + self._pin + '\n'
        result += 'Balance: ' + str(self._balance)
        return result

    def get_balance(self) -> float:
        """
        Returns the current balance.
        :return The current balance of this SavingsAccount is returned.
        """
        return self._balance

    def get_name(self) -> str:
        """
        Returns the current name.
        :return The name of the person who owns this SavingsAccount is returned.
        """
        return self._name

    def get_pin(self) -> str:
        """
        Returns the current pin.
        :return The pin number of this SavingsAccount is returned.
        """
        return self._pin

    def deposit(self, amount) -> None:
        """
        If the amount is valid, adds it to the balance and returns None; otherwise, returns an error message.
        :param amount: The amount to deposit into this SavingsAccount
        :return None
        """
        self._balance += amount
        return None

    def withdraw(self, amount):
        """
        If the amount is valid, subtract it from the balance and returns None; otherwise, returns an error message.
        :param amount: The amount to withdraw from this SavingsAccount
        :return An error message is returned if the amount is less than 0 or if there are insufficient funds; otherwise
        None is returned.
        """
        if amount < 0:
            return "Amount must be >= 0"
        elif self._balance < amount:
            return "Insufficient funds"
        else:
            self._balance -= amount
            return None

    def compute_interest(self) -> float:
        """
        Computes, deposits, and returns the interest.
        :return The amount of interest computed and deposited is returned.
        """
        interest = self._balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest
