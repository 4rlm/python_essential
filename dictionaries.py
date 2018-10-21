## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_dictionaries.asp

## == Note About Collections ==
# There are four collection data types in the Python programming language:
# List []            # Ordered and changeable. Allows duplicate members.
# Tuple ()           # Ordered and unchangeable. Allows duplicate members.
# Set {}             # Unordered and unindexed. No duplicate members.
# Dictionary {}      # Unordered, changeable and indexed. No duplicate members.
####################################


## 1. == Create & Access Dict
cars =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

cars2 =	dict(brand="Ford", model="Mustang", year=1964)  # dict() Constructor
car_tuples = cars.items()	                            # Returns list of tuples for each k-v pair
car_keys = cars.keys()	                                # Returns list of dictionary's keys
car_vals = cars.values()	                            # Returns list of dictionary's values
model = cars["model"]                                   # Access Dict item by key
model = cars.get("model")                               # Access Dict item by 'get' method and key
####################################


## 2. == Manipulate Dict - Simple
cars["year"] = 2018                                # Change item value by key
copied = cars.copy()	                           # Returns copy of dict

number_of_cars = len(cars)                         # Length
cars["color"] = "red"                              # Add Item (key-value pair)
cars.pop("model")                                  # Remove Item
cars.popitem()                                     # Removes Random Item
del cars["model"]                                  # Removes Item w/ Key
del cars                                           # Delete entire Dict from memory w/ 'del'.
cars.clear()                                       # Empties entire Dict.
####################################


## 3. == Manipulate Dict - Advanced
x = ('key1', 'key2', 'key3')
y = 0
dict_from_keys = dict.fromkeys(x, y)           # Create dict w 3 keys, all w value 0.

bronco = cars.setdefault("model", "Bronco")    # Returns val of key. Inserts key, w val if key doesn't exist.
cars.update({"color": "White"})                # Updates dict w key-val pairs
####################################


## 3. == Loop Through Dict:  for loop
for x in cars:
  print(x)                      ## Returns each 'key-value'.

for x in cars:
  print(cars[x])                ## Returns each 'value'.

for x in cars.values():
  print(x)                      ## Returns each 'value'.

for x, y in cars.items():
  print(x, y)                   ## Returns each 'key-value'.
####################################


## 4. == Check if el Exists:  in
if "model" in cars:
  print("Yes, cars dictionary has a 'model' key.")
####################################
