str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

def does_have_dino(my_string):
    return my_string.find("Dino") >= 0

print(does_have_dino(str1))
print(does_have_dino(str2))

# better solution
'Dino' in str1  # False
'Dino' in str2  # True