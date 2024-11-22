
# 1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Updating values
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

# Display updated values
print("Updated x:", x)  # [[5, 2, 3], [15, 8, 9]]
print("Updated students:", students)  # [{'first_name': 'Michael', 'last_name': 'Bryant'}, ...]
print("Updated sports_directory:", sports_directory)  # {'basketball': [...], 'soccer': ['Andres', ...]}
print("Updated z:", z)  # [{'x': 10, 'y': 30}]

# 2. Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ", ".join([f"{key} - {value}" for key, value in dictionary.items()])
        print(output)

# Testing iterateDictionary
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

print("\nIterate Through a List of Dictionaries:")
iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

# Testing iterateDictionary2
print("\nValues for 'first_name':")
iterateDictionary2('first_name', students)
print("\nValues for 'last_name':")
iterateDictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, value_list in some_dict.items():
        print(f"{len(value_list)} {key.upper()}")
        for value in value_list:
            print(value)
        print()  # Add a blank line for better readability

# Testing printInfo
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print("\nIterate Through a Dictionary with List Values:")
printInfo(dojo)
