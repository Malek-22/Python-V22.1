# Countdown - Accept a number as input and return a list counting down from that number to 0
def countdown(number):
    return list(range(number, -1, -1))
print(countdown(5))  # output: [5, 4, 3, 2, 1, 0]

# Print and Return - Print the first value and return the second value of a list
def print_and_return(my_list):
    print(my_list[0])  # Print the first value
    return my_list[1]  # Return the second value
print(print_and_return([1, 2]))  # output: 1 (printed), returns 2

# First Plus Length - Return the sum of the first value in the list plus the length of the list
def first_plus_length(my_list):
    return my_list[0] + len(my_list)
print(first_plus_length([1, 2, 3, 4, 5]))  # output: 6

# Values Greater than Second - Return a new list containing values greater than the second value and print how many values are greater
def values_greater_than_second(my_list):
    if len(my_list) < 2:
        return False
    second_value = my_list[1]
    greater_than_second = [value for value in my_list if value > second_value]
    print(len(greater_than_second))  # Print how many values are greater
    return greater_than_second
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))  # output: 3 (printed), returns [5, 3, 4]
print(values_greater_than_second([3]))  # output: False

# This Length, That Value - Create a list of a given size, filled with a given value
def length_and_value(size, value):
    return [value] * size
print(length_and_value(4, 7))  # output: [7, 7, 7, 7]
print(length_and_value(6, 2))  # output: [2, 2, 2, 2, 2, 2]

