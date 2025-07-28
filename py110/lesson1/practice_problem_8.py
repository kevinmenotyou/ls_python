statement = "The Flintstones Rock"
statement = statement.replace(' ', '')

my_dict = {}
for letter in statement:
    print (letter)

    # dict.get(letter, DEFAULT_VALUE) can also be used here

    if letter not in my_dict:
        my_dict[f"{letter}"] = 0
    my_dict[f"{letter}"] += 1

print (my_dict)