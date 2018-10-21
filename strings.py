## W3 Schools TUTORIAL: https://www.w3schools.com/python/python_strings.asp
####################################


## 1. == Strings ==
greeting = "Hello"
msg = "Hello, World!"
substr_1 = msg[1]  ## Substring. Gets character at position 1
substr_2 = msg[2:5]  ## Substring. Gets characters from position 2 to position 5 (not included)
msg_stripped = msg.strip()  ## Removes any whitespace from the beginning or the end
msg_len = len(msg)  ## Returns length of string
msg_lower = msg.lower()  ## Returns string in lower case
msg_upper = msg.upper()  ## Returns string in upper case
msg_replaced = msg.replace("H", "J")  ## Replaces a string with another string
msg_parts = msg.split(",")  ## Returns ['Hello', ' World!']
####################################



## 2. == String Interpolation ==
name = "Adam"
age = 42
name_msg = f'Hello my name is {name}\n'
age_msg = f'I am {age} years old.\n'
print(name_msg + age_msg)
####################################
