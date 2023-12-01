
print('Helloo')

ef = 34879.89933

print(int(ef))
print(round(ef))

# Means put a seperate line
print('--------------------')

# 0b means binary (includes 2 values which is 0 and 1, works from right to left, every number is mutilped by the power of 2)
ab = 0b1001
print(ab)


a_int = 1
b_float = 1.0
c_sum = a_int + b_float
print(c_sum)
# Type means to show the type pf an object
print(type(c_sum))

a = 1
b = 1.2
c= a + b
print(c)
print(type(c))

c = 1.1 + a + b
print(c)
print(type(c))

a = 3
b = 2
c =float(a + b)
print(c)
print(type(c))

f = a + b
print('the price is: ' + str(f) + '$')

a=123
b = 456
c = a + b
print(c)

cd = 0b101
print(cd)

# 0x means a hax - from a to f is equal to from 10 to 15
x = 0xf
print(x)

N = 0b10
print(N)

v = 0xf
print(v)

a = 10
b = 2

c = a // b
print(c)
print(type(c))

#  % Means a reminder of divison( smth in math)
d = a % b
print(d)
print(type(d))

s2 = 'abcdefg'
print(s2)
print(len(s2))
print(type(s2))
print('this is letters : '+ s2)
# string starts with 0 for counting from the left while starts with -1 to count from the right
print(s2[5])
print(s2[-1])
# to get a specfic objects inside a string
print(s2[1:5])

s3 = "i Can't stand this"
print('My Quote: ' + s3)

s4 = 'I can\'t'
print(s4)

s5 = 'i can\'t "Pawel"'
print(s5)

s6 = "I Can't \"Pawel\""
print (s6)

# \n means a new line after it
s7 = 'hdsvdshv\njhfdsdghsd'
print(s7)

# \t means leave a space
s8 = 'sjdfsfjk\tcsfff'
print(s8)

# if you really want to use \ then we use \\
s10 = 'sjdfsfjk\\tcsfff'
print(s10)

# And if you really want to use n or t then you just add it
s7 = 'hdsvdshv\nnjhfdsdghsd'
print(s7)

# How to turn a whole charcter string into a list : we use \t to put space and split to split into lists
B = '1234\tabcd\txyzf'
print(B.split('\t'))

# Same with \n
A = '1234\nabcd'
print(A)
print(A.split('\n'))
print(A.splitlines())
print(A.split('\n')[0])




# ord means that we are looking for specific object inside ascii table
print(ord('A'))
print(ord('9'))



numbers = [1, 2, 3, 4, 5]
numbers.insert(0,-1)
print(numbers)

numbers = [1, 2, 3]
numbers.insert(1, 5)
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)

hiiiii


