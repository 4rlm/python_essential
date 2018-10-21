## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_arrays.asp
####################################

## == Note About Collections ==
# There are four collection data types in the Python programming language:
# List []            # Ordered and changeable. Allows duplicate members.
# Tuple ()           # Ordered and unchangeable. Allows duplicate members.
# Set {}             # Unordered and unindexed. No duplicate members.
# Dictionary {}      # Unordered, changeable and indexed. No duplicate members.
####################################

## 1. == Create & Access Lists
lis = ["apple", "banana", "cherry"]         # Create List A: Simple
lis = list(("apple", "banana", "cherry"))   # Create List B: list()
apple = lis[1]                              # Access List els by Index
lis_length = len(lis)                       # Get List Length
apple_count = count("apple")                # Counts Frequency of el
apple_index = index("apple")                # Gets Index of el
####################################


## 2. == Change & Manipulate Lists
lis[1] = "blackcurrant"                    # Change el Value
lis.append("orange")	                   # Adds an el at end of list
lis_2 = lis.copy()	                       # Returns copy of list
lis.extend("melon", "mango")	           # Add multiple els to end of list
lis.insert("kiwi", 2)	                   # Adds an el at index
sorted = lis.sort()	                       # Sorts list
reversed = lis.reverse()                   # Reverses order of list
lis.remove("Volvo")	                       # Removes first el with specified value
lis.pop(1)	                               # Removes el at index
del lis[0]                                 # Removes el at index
lis.clear()	                               # Removes all els from list
####################################


## 3. == Loop Through List:  for loop
for x in lis:
    print(x)
####################################


## 4. == Check if el Exists:  in
if "apple" in lis:
  print("Yes, 'apple' is in the fruits list")
####################################


## 5. == Car Example List ==
cars = ["Ford", "Volvo", "BMW"] # create
first_car = cars[0] # Access
cars[0] = "Toyota" # Modify
number_of_cars = len(cars) # Length
####################################
