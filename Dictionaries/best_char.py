#Create the dictionary characters that shows each character from the string sally and its frequency.
#Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.




sally = "sally sells sea shells by the sea shore"
characters = {}
for c in sally :
    characters[c] = characters.get(c,0)+1

    
best_char = list(characters.keys())[0]
for key in characters:
    if characters[key] > characters[best_char]:
        best_char = key
        
        
