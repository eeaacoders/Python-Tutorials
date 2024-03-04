# Operations on the string

# Slicing in the strings

str = "EACODE"

print(str[0:6])

# We can fiidn the length of the string by using the len() func

str1 = "Mangohastowsides"

print(len(str1))

str1 = len(str)
print(str1)
print("The Length of the str1 variable is: ",len(str))
#using the slicing method in the python
print(str[0:4])
print(str[1:4])
print(str[:4])  # Automatically attach zero at the left

# These two statements are the same
print(str[0:-3])
print(str[0:len(str)-3])