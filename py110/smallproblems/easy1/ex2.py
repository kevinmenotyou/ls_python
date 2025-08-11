def is_palindrome(my_string: str):
    my_reversed_string = list(my_string)
    my_reversed_string.reverse()
    my_reversed_string = "".join(my_reversed_string)
    return my_string == my_reversed_string

#def is_palindrome(s):
#    return s == s[::-1]

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

