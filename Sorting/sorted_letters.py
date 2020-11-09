#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.


letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters  = sorted(letters, reverse = True)  

#sorted function expects a sequence ,but we have passed a string ,so it will convert it into a list whose elements are character of the string, letters.


print(sorted_letters)
