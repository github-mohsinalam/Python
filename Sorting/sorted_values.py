#Sort the following dictionary’s keys based on the value from highest to lowest.
#Assign the resulting value to the variable sorted_values.



dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = []
y = sorted(dictionary.keys(), reverse = True, key = lambda k:dictionary[k])

for key in y:
    sorted_values.append(key)
    
print(sorted_values)

