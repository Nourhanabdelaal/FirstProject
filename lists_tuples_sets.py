print('----------------------LISTS------------------------------')
num_list = [2,4,3,7,6,8,10,9,5]
print(num_list)

num_list_squared = [x**2 for x in num_list]
print(num_list_squared)

num_list_sorted = sorted(num_list_squared)
print(num_list_sorted)

num_list_rev = sorted(num_list_squared, reverse= True)
print(num_list_rev)

num_list_to_set = set(num_list_squared)
print(num_list_to_set)

num_set_to_list = list(set(num_list_squared))
print(num_set_to_list)

print('----------------------TUPLES------------------------------')
tuple_list = [(1,2), (3,4), (5,6)]
# to print an item inside tuple in ()
print(tuple_list[0])
# to assign some variables for values inside my tuple list
x, y = tuple_list[1]
print(x, y)

t = (1, 5, 6)
print(t[1])

# this will give an error as t[1] = 5 and tuples are immutable and we cant change their values

#t[1] = 6
#print(t[1])

tuplelist = ('age', 30),('Name', 'Nourhan')
print(tuplelist[1])

print(list(zip(tuplelist)))

print('----------------------MATRIX------------------------------')
list_2D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]
print(list_2D[2])

for row in list_2D:
    print(row)

#TODO:
# 1. Sum each row of the matrix - create a list of those sums
# 2. Sum all elements
# 3. Sum each column of the matrix - create a list of those sums

#1.
list = []
for row in list_2D:
    #print(sum(row))
    list.append(sum(row))
print(list)

#2.
print(sum(list))

#3.
col_sum = [0, 0, 0]
for row in list_2D:
    for i in range(len(row)):
        col_sum[i] += row[i]
print(col_sum)

#Another solution

columns = list(zip(*list_2D))

columns_sum = [sum(col) for col in columns]
print(columns_sum)


#3. My answer

sum_col1 = 0
for col in list_2D:
    x = col[0]
    sum_col1 += x
print(sum_col1)

sum_col2 = 0
for col in list_2D:
    y = col[1]
    sum_col2 += y
print(sum_col2)

sum_col3 = 0
for col in list_2D:
    x = col[2]
    sum_col3 += x
print(sum_col3)

list_sum = [sum_col1, sum_col2, sum_col3]
print(list_sum)






