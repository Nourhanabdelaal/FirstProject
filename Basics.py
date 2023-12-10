print("-------------------------String--------------------------------")
# a string is considered one part ,we print by character
txt = "Hello World"
y = txt[0]

# or by range
txt = "Hello World"
y = txt[2:5]

# to print length of string
y = "Hello World"
print(len(y))

# Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
y = txt.strip()

# upper or lower same
txt = "Hello World"
txt = txt.upper()

# Replace :Replace the character H with a J.

txt = "Hello World"
txt = txt.replace("H", "J")

# Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print("-------------------------Lists--------------------------------")

# to print
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# to print the last item
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# to change value
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# to add smth to the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# to insert in some specific place
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

# to remove smth
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# to print the number of items
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

print("-------------------------tuple--------------------------------")

# to print
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# to print the number of items
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# to print last item
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# using range in tuple
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

print("-------------------------Sets--------------------------------")

# if ---- in
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# in sets we say add not append
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# how to add a whole list to a set ?
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# to remove ? same as lists
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# or discard
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

print("---------------------------------------Dict-------------------------")
# how to print or get a value from dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

# how to change a value in a dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

# how to add
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

# how to remove
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

# how to clear the dict
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

print("-----------------------------------if else-------------------------")

a = 50
b = 10
if a > b:
  print("Hello World")

# using else
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#  Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 5
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

# Using and / or with if
if a == b and a < 3:
  print("yes")

# Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").
print("yes") if a == b else print("no")

# Use an if statement to print "YES" if either a or b is equal to c.
a = 2
b = 50
c = 2
if c == a or b:
  print("y")


a = 2
b = 50
c = 2
if a == c or b ==c:
  print("yup")

print("-----------------------------------while loop -------------------------")
i = 1
while i < 2:
  print(i)
  i += 1

print("----------")
# Stop the loop if i is 3.
i = 0
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("====================")
#  In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# while and else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print("-----------------------------------For loop -------------------------")
# Means for a variable in a sequence, we just made that variable for that sequence
fruits = ["apple", "banana", "cherry"]
for y in fruits:
  print(y)
#(there is no x actually in the list but we just call variables with whtever, print as a list.

#In the loop, when the item value is "banana", jump directly to the next item.

for fruit in fruits:
  if fruit == "banana":
    continue
  print(fruit)

# Use the range function to loop through a code set 6 times.
for y in range (6):
  print(y)

fruits = ["apple", "banana", "cherry"]
for y in fruits:
  if y == "banana":
    break
  print(y)

print("-----------------------------------Functions -------------------------")
# Execute a function named my_function.
def my_function(value):
  return value
print(my_function(1))

def myvalue():
  print("hello myvalue")


myvalue()
# * returns indefinte number of values in a tuple
def hello(*numbers):
  return numbers
print(hello(1, 2, 3))

# ** returns values in a dict
def helloo(**numbers):
  return numbers

print(helloo(name = "Nourhan", age = "25"))


# lambda
# classes
# inheritance
# modules


