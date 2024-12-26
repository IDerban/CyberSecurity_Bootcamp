# Assignment 4 - Iterations
# Task 1 - Create a python file "while.py"
# Create a program that continually ask user to enter a number
# Exit loop if user enters -1
# Calculate the average of all valid numbers entered.
# While loop is used for continuos prompting and number collection.

"""
PSEUDOCODE
1. Assign variables for collection of numbers
2. Create a while loop
3. Use if statement to check if user has entered the valid number
4. Calculate the average of the valid number entered.
"""

# Declare variable for collecting numbers from user.
valid_number = int(input("Enter a Random Number \n"))# Accepts numbers as integers
while valid_number==0:
 valid_number = int(input("Enter a Random Number \n")) # Asks User to enter a new number
 if valid_number >=1: # Checks if number is greater than 0
  print (f"The average value of the number entered is {valid_number/2} \n") #Calculate and display the average value of the number entered.
  valid_number = int(input("Enter a Random Number \n")) # Asks User to enter a new number

 if valid_number <0: # Checks if number is less than 0
  #print("You have Entered an Invalid Number")
  break # stops the program if the number is less than o
