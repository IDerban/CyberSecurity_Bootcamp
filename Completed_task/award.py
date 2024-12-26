# Assignment 3 - Task 3
# award.py file created.
# Create a program to intereact with user


####### PSEUDOCODE BELOW ##############

""" PSEUDOCODE BELOW 

1. Scope: Design a program that determines the award a person competing in a triathlon will receive.
2. Declare and assign variables to the 3 events: Swimming, Cycling, Running
3. Record, Calculate and display the total time a participant used to complete all three events.
4. Design the criteria for awarding a participant based on the time of completing all three events.
    a. Honorary colours          =>     Within the qualifying time : 0-100 minutes
    b. Honorary half colours     =>     Within five minutes of the qualifying time. : 101-105 minutes
    c. Honorary scroll           =>     Within 10 minutes of the qualifying time. : 106-110 minutes
    d. No award                  =>     More than 10 minutes off from the qualifying time. : 111+ minutes
"""

############# TASK 3 ########################
#Declaration of variables
swimming = int(input("Time for Swimming Event in minutes \n")) # Accepts Time for completion of swimming event
cycling = int(input("Time for Cycling Event in minutes \n")) # Accepts Time for completion of cycling event
running = int(input("Time for Running Event in minutes \n")) # Accepts Time for completion of running event
total_event = (swimming+cycling+running) # Total time completed for Triathlon
print(f"The total time to complete the Trianthlon is {total_event} minutes") # Display the Total time used to complete the Trianthlon

# Determine the award for the participant based on the total time to complete the trianthlon
# Use if, elif and els statement

if total_event <=100:    # Checks if the total time is less than 100 minutes
    print("Congratulations, You are Awarded ""Honorary Colours."" \n Thank you for participating in this event.")
elif total_event  >100 and total_event <=106: # Checks if the total time is within 101 and 105 minutes
    print ("Congratulations, You qualify for ""Honorary half colours"" award. \n Thank you for participating in this event.")
elif total_event  >105 and total_event <=110: # Checks if the total time is within 106 and 110 minutes
    print ("Congratulations, Your qualify for ""Honorary Scroll"" award. \n Thank you for participating in this event.")
else: # if none of the above condition is met, the total completion time is more than 110 minutes; thus, no Award
    print ("Sorry, You do not qualify for an award. \n Thank you for participating in this event.")        


############ END OF ASSIGNMENT 3; TASK 3 ####################################