numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

new_list = []

for number in list(numbers.values()):
    new_list.append(int(number/2))

print (new_list)