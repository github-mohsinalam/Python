#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

with open("school_prompt.txt") as school_prompt:
    three = []
    for line in school_prompt:
        line = line.strip()
        three.append(line.split()[2])
print(three)
        
        
