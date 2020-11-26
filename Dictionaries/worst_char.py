#Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency.
#Then, find the least frequent letter in the string and assign the letter to the variable worst_char.



sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for c in sally :
    characters[c] = characters.get(c,0)+1
    

worst_char = list(characters.keys())[0]

for key in characters:
    if characters[key] < characters[worst_char]:
        worst_char = key
        
