lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

#P i: list, o: dict(k,v)
#E
#D
#A for each sublist, key = [0], value = [1]
#C

#result = [new_dict for sublist in lst for item in sublist if]

newdict = {}
for sublist in lst:
    newdict[sublist[0]]= sublist[1]

mydict = {}
[mydict.update({sublist[0]: sublist[1]}) for sublist in lst]
print (mydict)

# or also
# dict1 = {item[0]: item[1] for item in lst}
# print(dict1)

###
# Pretty printed for clarity
# {
#     'a': 1,
#     'b': 'two',
#     'sea': {'c': 3},
#     'D': ['a', 'b', 'c']
# }