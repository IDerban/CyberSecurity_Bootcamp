# Assignment 4 - Iterations
# Task 2 - Create a python file "pattern.py"
# Write a code to output an arrow pattern
# Use if-else statements and for loop

"""
PSEUDOCODE
1. Declare variable for storing string "star"
2. write a code to print out the star using for loop and if statements.
3. Write a code for decreasing order of the stars
4. Write a code for increasing order of the stars
5. Request a user to input number within the range of (1,6)
"""

# Declare variable for storing "*" string
star="*"
stars= "*****"
new_number = int(input("Enter Even number \n"))
new_number1 = int(input("Enter Odd number \n"))

if (new_number % 2 == 0) and (new_number1 % 2 !=0): # checks if new_number is Even Number and new_number1 is
    for i in range (0,5): # Loop when an Even number is entered
        print(star) # Displays the results from low to high
        star=star + "*" # Loops with an additon of * everytime the the for loop is true
    for i in range (0,5): # Displays the results when an Odd number is entered.
        i = 4 - i # Indexing from 0 - 4, in descending order
        print(stars[0:i]) # Displays results for descending order from high to low


    
      