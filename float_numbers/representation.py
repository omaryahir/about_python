

# CASE 1
print("CASE 1:")
x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}')   # <-- 0.999999999

# CASE 2
print("CASE 2:")
x = 0.0
for i in range(10):
    x += 0.1

if x < 1.0:
    print(f'x = {x}') # <-- with < condition is better for float numbers
else:
    print(f'x != {x}')  


# CASE 3
# another approach is to round the values
print("CASE 3:")
x = 0.0
for i in range(10):
    x += 0.1
x = round(x,1) # round to 1 decimal

if x == 1.0:
    print(f'x = {x}') # <-- now we have 1
else:
    print(f'x != {x}')  


