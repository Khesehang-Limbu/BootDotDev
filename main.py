"""

Protecting Bank Information
Age of Dragons is a game about resource management and strategy. The game has a feature that allows players to manage their resources in a bank. The bank has a feature that allows players to deposit and withdraw funds.

Assignment
Complete the BankAccount class.

Complete the constructor
Set __account_number to account_number
Set __balance to initial_balance
Complete the public getters
Complete the get_account_number method to get the value of the private variable __account_number and return it.
Complete the get_balance method to get the value of the private variable __balance and return it.
Complete the deposit method
It should accept an amount as input and add it to the account balance.
If the deposit amount isn't positive, it should raise a ValueError exception with the message cannot deposit zero or negative funds. Otherwise, it should add the amount to the balance.
Complete the withdraw method
It should accept an amount and check if there is enough money in the account for the withdrawal.
If the withdrawal amount isn't positive, it should raise a ValueError exception with the message cannot withdraw zero or negative funds. Then, if there are not enough funds it should raise a ValueError exception with the message insufficient funds. Otherwise, it should deduct the amount from the balance.

"""

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")

        if not self.get_balance() >= amount:
            raise ValueError("insufficient funds")

        self.__balance -= amount

