lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

#[[], [3, 12], [9], [15, 18]]

def getMultiplesOfThree(sublist):
    return [item for item in sublist if item % 3 == 0]

my_result = [getMultiplesOfThree(sublist) for sublist in lst ]

my_one_liner = [[num for num in sublist if num % 3 == 0] for sublist in lst] # nested comprehension

print (my_result)
print(my_one_liner)