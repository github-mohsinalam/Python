#Assign to the variable num_lines the number of lines in the file school_prompt.txt.


num_lines = 0
with open('school_prompt.txt') as school_prompt:
    for line in school_prompt.readlines():
        num_lines +=1
        
