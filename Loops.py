# Note that range stops at the last object before the one you mentioned
for i in range(0, 5):
    print('i')
    print(f'i={i}')

for N in range(0, 3):
    print(f'N={N}')

# We can use range to increment(increase numbers by 1 or 2 or 3)
for M in range(0,5,3):
    print(f'M={M}')

for H in range(0, 10, 2):
    print(f'H= {H}')

for T in range(0, -2):
    print(f'T = {T}')

# We use reversed when we use a negative numbers

for items in reversed(range(-5, 10, 2)):
    print('Items: ' + str(items))

# It also used with strings
for chart in 'abcdef':
    print(f'chart={chart}')

# While loop we identify a condition and we have to specify the value of that condition sepratly
# we use incrementation which is a condition, otherwise the loop will keep running
l = 2
while l < 10:
    print(l)
    l = l + 1
# if the condition of while is not valid then the code wont run actually
B = 3
while B > 5:
    print(B)
# (see it won't run)


w = 2
while w < 10:
    w = w + 1
    if w == 4:
        continue
    if w == 8:
        break
    print('w= ' + str(w))













































































