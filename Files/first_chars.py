#Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

with open("travel_plans.txt") as travel_plans :
    first_chars = travel_plans.read(33)
