# Assignment 3 - Task 1
# manipulation.py file created.
# Create a program to intereact with user


####### PSEUDOCODE BELOW ##############

""" PSEUDOCODE BELOW 

1. Create variable called str_manip
2. Ask user to enter a sentence
3. Calculate and display the length of the sentence typed by the User
4. Replace the last letter in the sentence with @
5. Display last three characters in str_manip backwards.
6. Create a five - letter word made up of the first three characters and last two characters in str_manip

"""

######## TASK 1 ##########
"""
Variables to declare and  use

str_manip       : accepts users input - sentence
str_manip_1     : calculates the total number of characters in the sentence
str_manip_last  : is the last letter in the sentence  
str_manip_l3    : gives the last 3 letters in the sentence spelt backwards
str_manip_3     : counts the first three (3) letters in the sentence
str_manip_l2    : gives the last 2 letters in the sentence

"""
# Declare variable
str_manip = input(""" Type a sentence here  \n""") #This variable accepts long sentences

# Calculate and Display the length of the sentence
# Declare new variable to calculate and display the length of the sentence (Total Characters)
str_manip_1 = len(str_manip) # This variable calculates the length of the sentence typed which is equal to the total characters
print(f"{str_manip_1} is the total number of characters in your sentence, including spaces") # This displays the outcome of the calculations done.

#Find the last letter in the sentence
# Declare variable to store the last letter
str_manip_last = str_manip[-1:] # Stores the last letter
print(f"The last letter in your sentence is {str_manip_last}") # This displays the last letter in the sentence.

# Replace the last letter in the sentence with @
# Display the new sentence formed.
# Use f- string to construct a sentence.
print(f"The last letter in your sentence has been replaced with @ and the new sentence becomes \n  {str_manip.replace(str_manip_last,"@")}" ) 

# Display the last three characters in str_manip backwards.
# Find the total characters
# Use extended slice to find the last 3 letter backwards.
# Use f-string to tell the user the last 3 letters spelt backwards.
"""This finds the total characters, counts 4 letters backwards but excludes the last 4th letter"""
str_manip_l3 = str_manip[str_manip_1:-4:-1]
print(f"The last three (3) letters in your sentence spelt backwards is {str_manip_l3}") 

# Create a five - letter word made up of the first three characters and last two characters in str_manip
""" 
First three (3) characters in the sentence
use Extended slice to count from index 0 to the 3rd letter and include the first letter
slice the string to start from the last 2 characters and include the last letter without reserving the order
combine the first Three (3) characters and the last two (2) characters.
"""
# Declare variable to store the 1st three (3) letters in the sentence
str_manip_3 = str_manip[0:3:1] #Extended slice counts from index 0 (blank to the left of the first letter) to the 3rd letter and include the first letter
str_manip_l2 = str_manip[-2:] # Slice to begin from the last 2 characters and includes the last letter without reserving the order
# Combine the first Three (3) characters and the last two (2) characters.
# Display the final outcome to user using f-string

print(f"Combining the First 3 letters and last 2 letters gives us \n {str_manip_3}{str_manip_l2}") #Combines the First 3 and last 2 letters in the sentence.



########## END OF ASSIGNMENT 3, TASK 1 ######################################