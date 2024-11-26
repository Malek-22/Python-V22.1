class BankAccount:
    # Initialize with interest rate and balance
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
    
    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        return self  # Allows method chaining
    
    # Withdraw method
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self  # Allows method chaining
    
    # Display account info
    def display_account_info(self):
        print(f"Balance: ${self.balance:.2f}")
        return self  # Allows method chaining
    
    # Yield interest
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self  # Allows method chaining

# Create two accounts
account1 = BankAccount(int_rate=0.02, balance=100)
account2 = BankAccount(int_rate=0.03, balance=200)

# Perform operations for account1
account1.deposit(50).deposit(25).deposit(75).withdraw(100).yield_interest().display_account_info()

# Perform operations for account2
account2.deposit(100).deposit(50).withdraw(30).withdraw(20).withdraw(50).withdraw(10).yield_interest().display_account_info()

# Ninja bonus: Track all instances and display their info
class BankAccountWithTracking(BankAccount):
    # Class-level attribute to track all accounts
    accounts = []

    def __init__(self, int_rate=0.01, balance=0):
        super().__init__(int_rate, balance)
        BankAccountWithTracking.accounts.append(self)

    @classmethod
    def display_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

# Example for bonus:
bonus_account1 = BankAccountWithTracking(int_rate=0.01, balance=500)
bonus_account2 = BankAccountWithTracking(int_rate=0.05, balance=1000)

bonus_account1.deposit(100).withdraw(50).yield_interest()
bonus_account2.deposit(200).withdraw(100).yield_interest()

BankAccountWithTracking.display_all_accounts()
