lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def getSortedList(lst):
    return sorted(lst, key=getSumOfOdd)

def getSumOfOdd(sublist):
    return sum([item for item in sublist if item % 2 != 0])

my_great_result = getSortedList(lst)

print (my_great_result)