# Countdown - This function returns a list counting down from the number to 0
def countdown(number):
    return list(range(number, -1, -1))
print(countdown(5))  # output: [5, 4, 3, 2, 1, 0]

# Print and Return - This function prints the first number and returns the second def print_and_return(my_list):
    print(my_list[0])  # Print the first value
    return my_list[1]  # Return the second value
print(print_and_return([1, 2]))  # output: 1 (printed), returns 2

# First Plus Length - This function returns the first number plus the length of the list
def first_plus_length(my_list):
    return my_list[0] + len(my_list)
print(first_plus_length([1, 2, 3, 4, 5]))  # output: 6

# Values Greater than Second - This function returns numbers greater than the second number in the list
# If the list has less than 2 elements, it returns False
def values_greater_than_second(my_list):
    if len(my_list) < 2:
        return False
    second_value = my_list[1]
    greater_than_second = [value for value in my_list if value > second_value]
    print(len(greater_than_second))  # Print how many values are greater
    return greater_than_second
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  # output: 3 (printed), returns [5, 3, 4]
print(values_greater_than_second([3]))  # output: False

# This Length, That Value - This function returns a list of the given length, filled with the given value
def length_and_value(size, value):
    return [value] * size
print(length_and_value(4, 7))  # output: [7, 7, 7, 7]
print(length_and_value(6, 2))  # output: [2, 2, 2, 2, 2, 2]

