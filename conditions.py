## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_conditions.asp
####################################

## 1. == Conditions Intro ==
# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
# a == b          # Equals
# a != b          # Not Equals
# a < b           # Less than
# a <= b          # Less than or equal to
# a > b           # Greater than
# a >= b          # Greater than or equal to
####################################


## 2. == If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")
####################################


## 3. == Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
####################################


## 4. == Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

## can also have an else without the elif:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
####################################


## 6. == Short Hand If
if a > b: print("a is greater than b")
####################################


## 7. == Short Hand If ... Else
print("A") if a > b else print("B")
####################################


## 8. == One line if else statement, with 3 conditions:
print("A") if a > b else print("=") if a == b else print("B")
####################################


## 9. == And
if a > b and c > a:
  print("Both conditions are True")
####################################


## 10. == Or
if a > b or a > c:
  print("At least one of the conditions are True")
####################################
