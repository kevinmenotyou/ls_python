ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

my_sum = 0
for value in ages.values():
    my_sum += value

# BETTER SOLUTION
# my_sum = sum (ages.values())

print (my_sum)