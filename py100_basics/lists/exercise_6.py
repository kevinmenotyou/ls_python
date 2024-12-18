vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...

def print2dlist (my_2d_list):
    for first_list in my_2d_list:
        for item in first_list:
            print (item)

print2dlist(vocabulary)