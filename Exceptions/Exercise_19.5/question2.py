#The code below assigns the 5th letter of each word in food to the new list fifth.
#However, the code currently produces errors. Insert a try/except clause that will
#allow the code to run and produce of list of the 5th letter in each word.
#If the word is not long enough, it should not print anything out.
#Note: The pass statement is a null operation; nothing will happen when it executes.






food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for item in food :
    try:
        fifth.append(item[4])
    except:
        pass

