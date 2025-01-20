my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy() # shallow copy
my_list2[0]['first'] = 42
print(my_list1)

# lists are mutable
# copy is a /shallow/ copy of a new list
# however objects stored in the list point to their original memory location
# so a single reference is changed, which is referenced in both lists
# therefore the first list shows the new value as well

# Deep Copy
# makes a duplicate of every item in an existing list, including new instances of objects

# Shallow Copy
# makes a duplicate of the first layer of depth of an object with nested values