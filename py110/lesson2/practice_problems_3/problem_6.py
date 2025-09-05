lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_list = {(key, value + 1) for dict in lst for key, value in dict.items()}
# output - [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# Better solution:
# - use dict.items()

# def increment_values(dictionary):
#     return {key: value + 1 for key, value in dictionary.items()}

# new_list = [increment_values(value) for value in lst]

# print(new_list, lst, sep='\n')
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
# [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# One-liner:
# new_list = [{key: value + 1 for key, value in dictionary.items()}
#                            for dictionary in lst]

print(lst)
print(new_list)