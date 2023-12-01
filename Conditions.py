p = True
q = True

# And: Means that both of the 2 are true
if p and q:
    print('p and q True')
else:
    print('p and q False')
# OR: indicates that at least one is true
if p or q:
    print('p or q True')
else:
    print('p or q False')
# XOR : consider it like 2 horses in a race, both cant win and both cant lose so only one to win and one to lose
if p ^ q:
    print('p xor q True')
else:
    print('p xor q False')
# Not
if not p and q:
    print('not p and q True')
else:
    print('not p and q False')

if not p or q:
    print('not p or q True')
else:
    print('not p or q False')

    print('------------------')
a = True
print(a)

# We cant assign a bool to a value but we can assign a value to a bool
# True = 2
# print(True)

print('------------------')
# Comparisons
a = 10
b = 9

if a > b:
    print('a>b')
else:
    print('not a>b')

# We can't assign just an (=) value beacuse this = assign a value from the right hand side to the left hand side
if a == b:
    print('a=b')
else:
     print('not a=b')

#  greater or smaller then equal comes
a >= 3

if a > 4:
    print(True)
else:
    print(False)

s1 = 'abc'
s2 = 'nmr'

if s1 == s2:
    print('s1=s2')
else:
    print('s1!=s2')

# Another Way to write if
y = 100 if s1==s2 else 10
print(y)

if s1==s2:
    print('y: 100')
else:
    print(10)

# Multiple - switch operator - if you have multiple cases (match)- underscore means match anything else.
mv = 500

match mv:
    case 100:
        print('mv:100')
    case 200:
        print('mv:200')
    case _:
        print('mv is different')














