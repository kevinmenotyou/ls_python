numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# way 1
my_list = numbers.copy()
my_list.reverse()
print(my_list)

# way 2
my_other_list = numbers[0:len(numbers)]
my_other_list.reverse()
print (my_other_list)

# original list
print(numbers)

# launch school solution
reversed_numbers = numbers[::-1] # slice
reversed_numbers = list(reversed(numbers)) # cast