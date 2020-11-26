#Create a list called destination using the data stored in travel_plans.txt.
#Each element of the list should contain a line from the file that lists a country and cities inside that country.
#Hint: each line that has this information also has a colon : in it.


with open("travel_plans.txt") as travel_plans:
    destination = []
    for line in travel_plans :
        
        if ":" in line :
            destination.append(line)
print(destination)
            
        

