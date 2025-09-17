lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

[{'e': [8], 'f': [6, 10]}] # all even

# Input - List of Dictionaries
# Output - List of Dictionaries, every value is even across all items

def all_dict_even(dict_to_check):
    return all(all_list_even(value_list) for value_list in dict_to_check.values())

def all_list_even(value_list):
    return all(value % 2 == 0 for value in value_list)

new_list = [dictionary for dictionary in lst if all_dict_even(dictionary)]

print(new_list)