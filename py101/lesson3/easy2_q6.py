import math

TOTAL_LENGTH = 40

title = "Flintstone Family Members"

length_title = len(title)
print (f"Can center: {length_title % 2 == 0}")

number_of_spaces = math.floor((TOTAL_LENGTH - length_title) / 2)

my_spaces = ""
for _ in range(number_of_spaces):
    my_spaces += " "

print (my_spaces + title)

# Launch School Solution
centered_title = title.center(40)
print (centered_title)
