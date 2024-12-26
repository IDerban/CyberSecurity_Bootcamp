# Task 2
# Create a python file named "conversion.py"
# Declare the variables as provided

# Convert the variables as provided

"""
Pseudocode for Task 2
1. Declare the variables by determining it name and data type.
2. Convert the variables to different data type using casting.
3. Print all variables on separate lines

"""

############ DECLARE THE VARIABLES ########################

# Declare the variables by determing it name and data type.
# The variable num1 is a float becuase is has decimal point and no quotation marks
num1 = 99.23
# The variable num2 is an integer becuase it's a whole number and lacks quotation marks
num2 = 23
# The variable num3 is an integer becuase it's a whole number and lacks quotation marks
num3 = 150
# The variable string1 is a string becuase it has quotation marks
string1 = "100"

#The type () function can also be used to determine the data type of a variable
print(type(num1))
print(type(num2))
print(type(num3))
print(type(string1))

##########################################################



############## CONVERT THE VARIABLES #####################

"""
num1 into an integer
num2 into a float
num3 into a string
string1 into an integer

"""

# Convert num1 to integer.
# num1 is assigned as a float
# num1 can be converted to integer by casting
# num1 is a float
num1 = 99.23        
# use int () to convert float to integer
num1 = int(num1)    # this convert num1 to integer



# Convert num2 to float.
# num2 is assigned as an integer
# num12 can be converted to float by casting
# num2 is an integer
num2 = 23        
# use float () to convert integer to float
num2 = float(num2)    # this convert num2 to float


# Convert num3 to integer.
# num3 is assigned as an integer
# no need to convert to integer, python recognises it as an integer
num3 = 150       


# Convert string1 to integer.
# string1 is assigned as a string
# string1 can be converted to integer by casting since it value is an integer

string1 = "100"       # num1 is a float
# use int () to convert string1  to integer
string1 = int(string1)    # this convert num1 to integer
########################################################

############# PRINT VARIABLES ON SEPARATE LINES ##############

# Convert num1 to integer.
num1 = 99.23        
# use int () to convert float to integer
num1 = int(num1)    # this convert num1 to integer
print(int(num1))


# Convert num2 to float.
num2 = 23        
# use float () to convert integer to float
num2 = float(num2)    # this convert num2 to float
print(float(num2))


# Convert num3 to integer.
# num3 is assigned as an integer
# no need to convert to integer, python recognises it as an integer
num3 = 150       
print(num3)

# Convert string1 to integer.
string1 = int(string1)    # this convert num1 to integer
print(int(string1))

#########################################################################