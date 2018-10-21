## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_tuples.asp
####################################

## == Note About Collections ==
# There are four collection data types in the Python programming language:
# List []            # Ordered and changeable. Allows duplicate members.
# Tuple ()           # Ordered and unchangeable. Allows duplicate members.
# Set {}             # Unordered and unindexed. No duplicate members.
# Dictionary {}      # Unordered, changeable and indexed. No duplicate members.
####################################


## 1. == Create and Access Tuples
tup = ("apple", "banana", "cherry")           ## Create Tuple A: Simple
tup = tuple(("apple", "banana", "cherry"))    ## Create Tuple B: tuple()
apple = tup[1]                                ## Access Tuple Items by Index
tup_length = len(tup)                         ## Get Tuple Length
apple_count = count("apple")                  ## Counts Frequency of Item
apple_index = index("apple")                  ## Gets Index of Item
####################################


## 2. Forbidden Actions: add, remove, or change  ## Tuples are unchangeable.
tup[1] = "blackcurrant"                       ## Can't change value.
tup[3] = "orange"                             ## Can't add item.
del tup               ## Can't remove items, but can delete entire tuple from memory.
####################################


## 3. == Loop Through a Tuple: for loop
for x in tup:
  print(x)
####################################


## 4. == Check if Item Exists: in
if "apple" in tup:
  print("Yes, 'apple' is in the fruits tuple")
####################################
