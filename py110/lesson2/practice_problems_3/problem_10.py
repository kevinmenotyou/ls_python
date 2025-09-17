import random
import string

# Function:
# Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string. 
# The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

# Numbers: 31-39 ## 10
# Lower Case Letters: 61-69, 6a-6f, 70-79, 7a ## 26

def get_random_letter_or_number():
    random_integer = (random.randint(0, 14))
    if random_integer <= 9:
        return str(random_integer)
    else:
        return get_random_hex_letter()

def get_random_hex_letter():
    random_integer = (random.randint(0, 5))
    return string.ascii_lowercase[random_integer]

def generate_random_sequence(length):
    return [get_random_letter_or_number() for i in range (0,length)]

def generate_uuid():
    my_uuid = []
    my_uuid.extend(generate_random_sequence(8))
    my_uuid.append('-')
    my_uuid.extend(generate_random_sequence(4))
    my_uuid.append('-')
    my_uuid.extend(generate_random_sequence(4))
    my_uuid.append('-')
    my_uuid.extend(generate_random_sequence(4))
    my_uuid.append('-')
    my_uuid.extend(generate_random_sequence(12))
    return ''.join(my_uuid)

print (generate_uuid())