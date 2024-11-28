def is_empty_or_blank(my_string: str):
    #is null or whitespace
    return (len(my_string.strip()) == 0)


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True