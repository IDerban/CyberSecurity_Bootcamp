# Assignment 3 - Task 2
# numbers.py file created.
# Create a program to intereact with user


####### PSEUDOCODE BELOW ##############

""" PSEUDOCODE BELOW 

1. Create variable called str_manip
2. Creant three (3) variables num1, num2 and num3 to store integers
3. Ask user to type in numbers (integers) for each of the variables
4. Perform the following calculations using the values provided by the user
    a. The summ of all the numbers
    b. The first number minus the second number
    c. The third number multiplied by the first number
    d. The sum of all the numbers divided by the third number.

"""

# Declaration of variables : num1, num2, num3
num1 = int(input("Enter your First number \n"))                               # Accept First integer
num2 = int(input("Enter your Second number \n"))                              # Accept Second integer
num3 = int(input("Enter your Third number \n"))                               # Accept Third integer
total_num = int(num1+num2+num3)                                               # Sums up all the integers
# Display to user the request to Enter numbers
# Use f-string to form a sentence
print(f"Your first number is {num1}\n")                                     # Displays the first integer from the user
print(f"Your second number is {num2}\n")                                    # Displays the second integer from the user
print(f"Your third number is {num3}\n")                                     # Displays the third integer from the user

#calculation
#The sum of all the numbers
print(f"The sum of all numbers is {total_num}\n")                            # Sums up all the numbers provided by the user
#First number minus the second number
print(f"First number minus the Second number is {num1-num2}\n")              # This deducts the Second number from the First number
#Third number multiplied by the First number
print(f"The third number multiplied by the first number is {num1*num3}\n")   # This multiplies the Third number the the First number
#Third number multiplied by the First number
#Results must be an integer; convert a float into integer as the final result
print(f"The total sum divided by the third number is {int(total_num/num3)}\n")    # The sum of all the numbers divided by the third number
#Thanks the User for their cooperation
print("Thank you for participating in this project")

######### END OF ASSIGNMENT 3, TASK 2 ###############