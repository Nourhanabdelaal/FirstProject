my_file = 'Hello'

f = open(my_file, 'r')
lines = f.readlines()

i = 0
for line in lines:
    i += 1
    print(f'{i}: {line}', end='')

with open(my_file, 'r') as f:
    lines = f.readlines()
    i =0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end ='')