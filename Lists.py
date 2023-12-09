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
