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

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"Not enough points to spend {amount}. Current points: {self.gold_card_points}")
            return False
        self.gold_card_points -= amount
        print(f"Spent {amount} points. Remaining points: {self.gold_card_points}")
        return True



# Create the first user instance
user1 = User("Alice", "Smith", "alice.smith@example.com", 30)

# Display user1's info
print("User 1 Information:")
user1.display_info()

# Enroll user1 and display updated info
print("\nEnrolling User 1:")
user1.enroll()
user1.display_info()

# Have user1 spend 50 points
print("\nUser 1 Spending 50 Points:")
user1.spend_points(50)
user1.display_info()

# Create second and third user instances
user2 = User("Bob", "Johnson", "bob.johnson@example.com", 25)
user3 = User("Charlie", "Brown", "charlie.brown@example.com", 28)

# Display user2 and user3 info
print("\nUser 2 Information:")
user2.display_info()

print("\nUser 3 Information:")
user3.display_info()

# Enroll user2 and spend 80 points
print("\nEnrolling User 2:")
user2.enroll()
user2.spend_points(80)
user2.display_info()

# Attempt to re-enroll user1 (BONUS)
print("\nAttempting to Re-enroll User 1:")
user1.enroll()

# Attempt to overspend on user3 (BONUS)
print("\nUser 3 Attempting to Spend 40 Points:")
user3.spend_points(40)

# Final display of all users' information
print("\nFinal User 1 Information:")
user1.display_info()

print("\nFinal User 2 Information:")
user2.display_info()

print("\nFinal User 3 Information:")
user3.display_info()
