#Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.


with open('school_prompt.txt') as school_prompt:
    beginning_chars = school_prompt.read(30)
