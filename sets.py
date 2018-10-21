## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_sets.asp
####################################

## == Note About Collections ==
# There are four collection data types in the Python programming language:
# set []            # Ordered and changeable. Allows duplicate members.
# Tuple ()           # Ordered and unchangeable. Allows duplicate members.
# Set {}             # Unordered and unindexed. No duplicate members.
# Dictionary {}      # Unordered, changeable and indexed. No duplicate members.
####################################


## 1. == Create & Access Sets
set1 = {"apple", "banana", "cherry"}         # Create Set A: simple
set2 = set(("kiwi", "banana", "cherry"))    # Create Set B: set()
set_length = len(set1)                       # Get Length
####################################


## 2. == Manipulate Sets - Simple
set1.add("orange")                           # Add one item
set1.update(["orange", "mango", "grapes"])   # Add multiple items
last_item = set1.pop()                       # Removes last item in set
set1.remove("banana")                        # Remove item, error if doesn't exist.
set1.discard("banana")                       # Remove item, NO error if doesn't exist.
set1.clear()	                             # Removes all els from set
del set1                                     # Delete entire set from memory.
####################################


## 3. == Manipulate Sets - Advanced
copied = set.copy()	                         # Returns copy of list
dif = set1.difference(set2)	                 # Returns difference in new set
set1.difference_update(set2)                 # Removes items in set that are included in another
inter = set1.intersection(set2)              # Returns a set, that is intersection of two other sets
set1.intersection_update(set2)               # Removes items in set not present in other set
has_inter = set1.isdisjoint(set2)	         # Returns whether two sets have a intersection or not
is_sub = set1.issubset(set2)	             # Returns whether another set contains this set or not
is_sup = set1.issuperset(set2)	             # Returns whether this set contains another set or not
sym_dif = set1.symmetric_difference(set2)	 # Returns a set with the symmetric differences of two sets
set1.symmetric_difference_update(set2)	     # inserts the symmetric differences from this set and another
combined = set1.union(set2)	                 # Return a set containing the union of sets
####################################


## 4. Forbidden Actions
## Can't change set's els, but can add new els.
## Can't Access Set els by Index, but can loop.
## Can't remove items, but can delete entire set from memory w/ 'del set'
####################################


## 5. == Loop Through Set:  for loop
for x in set:
  print(x)
####################################


## 6. == Check if el Exists:  in
print("banana" in set)
####################################
