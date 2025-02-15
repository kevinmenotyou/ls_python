def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if not len(dot_separated_words) == 4:
        return False

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

def is_an_ip_number(word):
    number = int(word)
    return number >= 0 and number <=255

print(is_dot_separated_ip_address("123.45.6.744"))
print(is_dot_separated_ip_address("123.45.6.7"))
print(is_dot_separated_ip_address("123.45.6"))
print(is_dot_separated_ip_address("123.45.6.7.9"))