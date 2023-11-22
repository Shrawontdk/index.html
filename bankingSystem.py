class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return f"Account Balance: ${self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: ${interest}")

    def get_balance(self):
        return f"Account Balance: ${self.balance} (Interest Rate: {self.interest_rate * 100}%)"

# Creating instances of BankAccount and SavingsAccount
basic_account = BankAccount(account_number=12345, balance=1000)
savings_account = SavingsAccount(account_number=54321, balance=5000, interest_rate=0.02)

# Performing transactions
basic_account.deposit(500)
basic_account.withdraw(200)
print(basic_account.get_balance())

savings_account.deposit(1000)
savings_account.apply_interest()
savings_account.withdraw(500)
print(savings_account.get_balance())
