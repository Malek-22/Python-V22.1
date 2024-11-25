class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self  # Enable method chaining

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self  # Enable method chaining

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"Not enough points to spend {amount}. Current points: {self.gold_card_points}")
        else:
            self.gold_card_points -= amount
            print(f"Spent {amount} points. Remaining points: {self.gold_card_points}")
        return self  # Enable method chaining



# Create instances
user1 = User("Alice", "Smith", "alice.smith@example.com", 30)
user2 = User("Bob", "Johnson", "bob.johnson@example.com", 25)
user3 = User("Charlie", "Brown", "charlie.brown@example.com", 28)

# Method: chaining
print("Chaining methods for user1:")
user1.display_info().enroll().spend_points(50).display_info()

print("\nChaining methods for user2:")
user2.enroll().spend_points(80).display_info()

print("\nAttempting to overspend with user3:")
user3.display_info().spend_points(40)
