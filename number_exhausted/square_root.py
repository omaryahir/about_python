

# Finding the square root ...

target = int(input('Put a number: '))
value = 0 

while value**2 < target:
    value += 1
    print(f'Trying with value: {value}**2 = {value**2}')

if value**2 == target:
    print(f'\nThe square root of {target} is {value}')
else:
    print(f'\n{target} does not have a exact square root')
