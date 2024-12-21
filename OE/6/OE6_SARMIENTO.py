class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        self.__display_balance()
        return self.__balance

    def set_balance(self, balance: float):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Error: Balance cannot be negative.")

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Error: Insufficient funds or invalid withdrawal amount.")

    def display_account_info(self):
        print(f"Account Number: {self.get_account_number()}")
        print(f"Balance: {self.__balance:.2f}")

    def __display_balance(self):
        print(f"Current balance: {self.__balance:.2f}")

account = BankAccount("123456789", 1000.0)

account.display_account_info()

account.deposit(500.0)

account.withdraw(300.0)

account.set_balance(-200.0)

account.display_account_info()
