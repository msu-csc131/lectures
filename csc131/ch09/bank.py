"""
File: bank.py
This module defines the Bank class.
"""
import pickle
import random
from csc131.ch09.savings_account import SavingsAccount

class Bank:
    """This class represents a bank as a collection of savnings accounts.
    An optional file name is also associated
    with the bank, to allow transfer of accounts to and
    from permanent file storage."""

    # The state of the bank is a dictionary of accounts and
    # a file name.  If the file name is None, a file name
    # for the bank has not yet been established.

    def __init__(self, file_name = None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from
        a file of pickled accounts.
        :param file_name a file containing serialized pickled accounts
        """
        self._accounts = {}
        self._file_name = file_name
        if file_name != None:
            file_obj = open(file_name, 'rb')
            while True:
                try:
                    account = pickle.load(file_obj)
                    self.add(account)
                except Exception:
                    file_obj.close()
                    break

    def __str__(self):
        """Returns the string representation of the bank."""
        return "\n".join(map(str, self._accounts.values()))

    def _make_key(self, name, pin):
        """Returns a key for the account.
        :param name: the name of the owner of the account
        :param pin: the pin number of the account
        """
        return name + "/" + pin

    def add(self, account):
        """Adds the account to the bank.
        :param account: the account to add to this Bank
        """
        key = self._make_key(account.getName(), account.getPin())
        self._accounts[key] = account

    def remove(self, name, pin):
        """Removes the account from the bank and
        and returns it, or None if the account does
        not exist."""
        key = self._make_key(name, pin)
        return self._accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account from the bank,
        or returns None if the account does
        not exist."""
        key = self._make_key(name, pin)
        return self._accounts.get(key, None)

    def compute_interest(self):
        """Computes and returns the interest on
        all accounts."""
        total = 0
        for account in self._accounts.values():
            total += account.compute_interest()
        return total

    def get_keys(self):
        """Returns a sorted list of keys."""
        # Exercise
        return []

    def save(self, fileName = None):
        """Saves pickled accounts to a file.  The parameter
        allows the user to change file names."""
        if fileName != None:
            self._file_name = fileName
        elif self._file_name == None:
            return
        fileObj = open(self._file_name, 'wb')
        for account in self._accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()

# Functions for testing
       
def create_bank(num_accounts = 1):
    """Returns a new bank with the given number of 
    accounts."""
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia",
             "Ken", "Jill", "Jack")
    bank = Bank()
    upper_pin = num_accounts + 1000
    for pin_number in range(1000, upper_pin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pin_number), balance))
    return bank

def test_account():
    """Test function for savings account."""
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.get_balance())
    print(account.deposit(-50))
    print("Expect 600:", account.get_balance())
    print(account.withdraw(100))
    print("Expect 500:", account.get_balance())
    print(account.withdraw(-50))
    print("Expect 500:", account.get_balance())
    print(account.withdraw(100000))
    print("Expect 500:", account.get_balance())

def main(number = 10, fileName = None):
    """Creates and prints a bank, either from
    the optional file name argument or from the optional
    number."""
    test_account()
##    if fileName:
##        bank = Bank(fileName)
##    else:
##        bank = create_bank(number)
##    print(bank)

if __name__ == "__main__":
    main()

   
