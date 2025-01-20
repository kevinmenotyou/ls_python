def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

def is_colour_valid2(color):
    return color in ["blue", "green"]

def is_colour_valid3(color):
    return color == "blue" or color == "green"


print(is_colour_valid2("blue"))
print(is_colour_valid2("green"))
print(is_colour_valid2(1))
print(is_colour_valid2("red"))