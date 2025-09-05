dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

#input data structure
#output list of sublists and string
#colours of fruit - capitalized - [list]
#sizes of vegetables - uppercase - string

### LS SOLUTION

def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()

result = [transform_item(item) for item in dict1.values()]
print(result)

####

def processFruitsAndVegetables(my_fruit_or_veg_dict):
    return [capIfFruitAllCapIfVeg(value) for value in my_fruit_or_veg_dict.values()]

def capIfFruitAllCapIfVeg(my_item):
    if my_item['type'] == "vegetable":
        return allCapVegSize(my_item)
    elif my_item['type'] == "fruit":
        return capFruitColourList(my_item)
    raise Exception()

def capFruitColourList(my_fruit):
    return [capFruitColour(colour) for colour in my_fruit['colors']]

def capFruitColour(my_fruit):
    return my_fruit.upper()

def allCapVegSize(my_veg):
    return my_veg['size'].capitalize()

def allCaps(my_list):
    return [my_string.upper() for my_string in my_list]

my_new_data = processFruitsAndVegetables(dict1)
print (my_new_data)

def getSizeString(my_dict):
    return [value['size'] for key, value in my_dict.items() if value['type'] == "vegetable"]

def capitalizeSublist(my_list):
    return [capitalizeList(sublist) for sublist in my_list]

def capitalizeList(my_list):
    return [item.capitalize() for item in my_list]

def getColourList(my_dict):
    return [value['colors'] for key, value in my_dict.items() if value['type'] == "fruit"]