str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def my_function(my_string):
    return my_string[len(my_string) - 1] == "!"

print(my_function(str1))
print(my_function(str2))