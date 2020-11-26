#The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
#Find the total number of characters in the file and save to the variable num.



with open("travel_plans.txt") as travel_plans:
    num = len(travel_plans.read())
print(num)
