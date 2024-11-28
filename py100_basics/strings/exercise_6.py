def is_empty(my_string: str):
    #is null or whitespace
    return (len(my_string) == 0)


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True