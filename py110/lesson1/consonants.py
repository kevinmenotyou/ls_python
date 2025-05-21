import pdb

VOWELS = ('a', 'e', 'i', 'o', 'u')

def remove_spaces(my_string):
    my_new_string = ''
    for my_char in my_string:
        if not my_char.isspace():
            my_new_string += my_char
    return my_new_string

def count_max_adjacent_consonants(my_string):
    my_max_consonant_count = 0
    my_current_consonant_count = 0

    my_string = remove_spaces(my_string)
    
    for my_char in my_string:
        if my_char not in VOWELS:
            my_current_consonant_count += 1
        else:
            if my_current_consonant_count > my_max_consonant_count:
                my_max_consonant_count = my_current_consonant_count
                my_current_consonant_count = 0
    
    if my_current_consonant_count > my_max_consonant_count:
        my_max_consonant_count = my_current_consonant_count

    if (my_max_consonant_count <= 1):
        return 0

    return my_max_consonant_count 

def sort_by_consonant_count(my_list):
    my_list.sort(key=count_max_adjacent_consonants, reverse=True)
    return my_list

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

#Test Cases:
print(count_max_adjacent_consonants('dddaa'))       # 3
print(count_max_adjacent_consonants('ccaa'))        # 2
print(count_max_adjacent_consonants('baa'))         # 0
print(count_max_adjacent_consonants('aa'))          # 0
print(count_max_adjacent_consonants('rstafgdjecc')) # 4