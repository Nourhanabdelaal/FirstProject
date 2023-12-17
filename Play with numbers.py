num_list = [2, 5, 7, 9, 11, 13, 18]

""""'''
TODO
1. Print the subsequent 2nd powers of elements in the list
2. Sum the 2nd powers of elements of the list
'''"""

sum = 0

for num in num_list:
    x = num ** 2
    print(x)
    sum = sum + x
print('The Sum of 2nd power: ', sum)

print('-----------------------------------------------------')

# another solution:

for num in num_list:
    x = num ** 2
    print(x)

sum = sum(num ** 2 for num in num_list)
print(sum)

print('-----------------------------------------------------')

squared_list = []

for num in num_list:
    x = num ** 2
    squared_list.append(x)
print(squared_list)

sum_of_squared = sum(squared_list)
print("The sum of squared: ", sum_of_squared)

print('-----------------------------------------------------')

squared = []
for num in num_list:
    squared.append(num ** 2)
print(squared)

sum_squared = sum(squared)
print(sum_squared)


































