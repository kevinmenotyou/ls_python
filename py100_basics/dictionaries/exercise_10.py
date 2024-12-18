numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for pair in iter(numbers):
    print(f'A {pair} number is {numbers[pair]}.')

### LAUNCH SCHOOL SOLUTION
for key, value in numbers.items():
    print(f"A {key} number is {value}.")