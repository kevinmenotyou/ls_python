munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
 
    'Marilyn': {'age': 23,  'gender': 'female'},
}

my_sum = 0
for munster in munsters.values():
    print (munster)
    if munster['gender'] == 'male':
        print()
        #my_sum += munster['age']

all_male_ages = [munster['age'] for munster in munsters.values() if munster['gender'] == 'male']
my_sum = all_male_ages
print (my_sum)