class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {"default": BankAccount()}

    def add_account(self, account_name, int_rate=0.01, balance=0):
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self

    def make_deposit(self, amount, account_name="default"):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"Account '{account_name}' does not exist.")
        return self

    def make_withdrawal(self, amount, account_name="default"):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"Account '{account_name}' does not exist.")
        return self

    def display_user_balance(self, account_name="default"):
        if account_name in self.accounts:
            print(f"User: {self.name}, Account: {account_name}")
            self.accounts[account_name].display_account_info()
        else:
            print(f"Account '{account_name}' does not exist.")
        return self

    def transfer_money(self, amount, other_user, account_name="default"):
        if account_name in self.accounts:
            if self.accounts[account_name].balance >= amount:
                self.accounts[account_name].withdraw(amount)
                other_user.make_deposit(amount)
                print(f"Transferred ${amount} from {self.name}'s account to {other_user.name}'s account.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print(f"Account '{account_name}' does not exist.")
        return self


# Example Usage
user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")

# Adding multiple accounts for a user
user1.add_account("savings", int_rate=0.02, balance=500)

# Deposits
user1.make_deposit(200)
user1.make_deposit(300, "savings")

# Withdrawals
user1.make_withdrawal(50)
user1.make_withdrawal(100, "savings")

# Display Balances
user1.display_user_balance()
user1.display_user_balance("savings")

# Transfer Money
user1.transfer_money(100, user2, "savings")

# Display Balances After Transfer
user1.display_user_balance("savings")
user2.display_user_balance()
