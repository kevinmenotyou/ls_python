# launch school tech & talk
# so that you get the string 'Launch School Tech & Talk'

def capitalize_first (my_sentence: str):
    my_split_sentence = my_sentence.split(' ')
    my_list = []
    for word in my_split_sentence:
        my_item = word[0].upper() + word[1:len(word)]
        my_list.append(my_item)
    return (" ".join(my_list))

print (capitalize_first("launch school tech & talk"))