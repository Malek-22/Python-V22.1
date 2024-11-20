# This is my first Python assignment with for loops!
# Task 1: Print all integers from 0 to 150.
print("Task 1: Basic - Print all integers from 0 to 150")
for i in range(151):  # Loop through numbers 0 to 150
    print(i)

# Task 2: Print all multiples of 5 from 5 to 1,000.
print("\nTask 2: Multiples of Five")
for i in range(5, 1001, 5):  # Loop through numbers from 5 to 1000, step by 5
    print(i)

# Task 3: Print integers 1 to 100 with special conditions.
print("\nTask 3: Counting, the Dojo Way")
for i in range(1, 101):  # Loop through numbers 1 to 100
    if i % 10 == 0:  # If divisible by 10, print "Coding Dojo"
        print("Coding Dojo")
    elif i % 5 == 0:  # If divisible by 5, print "Coding"
        print("Coding")
    else:
        print(i)  # Otherwise, just print the number

# Task 4: Add odd integers from 0 to 500,000 and print the total sum.
print("\nTask 4: Whoa. That Sucker's Huge")
total_sum = 0
for i in range(1, 500001, 2):  # Loop through odd numbers from 1 to 500,000
    total_sum += i  # Add each odd number to the total
print(total_sum)  # Print the final sum

# Task 5: Countdown by fours from 2018.
print("\nTask 5: Countdown by Fours")
for i in range(2018, 0, -4):  # Loop down from 2018 to 0, step by -4
    print(i)

# Task 6: Flexible Counter
print("\nTask 6: Flexible Counter")
lowNum = 2  # Starting number
highNum = 9  # Ending number
mult = 3  # Multiple to check for
for i in range(lowNum, highNum + 1):  # Loop from lowNum to highNum
    if i % mult == 0:  # If the number is a multiple of mult
        print(i)  # Print the number
