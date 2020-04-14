
target = int(input('Choose a number: '))

# EPSILON
# Conventionally it's used to denote a small quantity, like an error, or 
# perhaps a term which will be taken to zero in some limit.
epsilon = 0.01 
step = epsilon**2
value = 0.0

while abs(value**2 - target) >= epsilon and value <= target:
    print(f'Trying value: {value} with target: {target}') 
    value += step

if abs(value**2 - target) >= epsilon:
    print(f'I can not find square root of {target}')
else:
    print(f'The square root of {target} is {value}')

