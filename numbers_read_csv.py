my_file = 'numbers.csv'

with open(my_file, 'r') as f:
    lines = f.readlines()

    i = 0
    for line in lines:
        line.split('\t')
        i +=1
        print(f'{i}:{line}', end='')
