#We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary input paramet
#then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.




def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

c_false =checkingIfIn('pine apple')                             # Call the function so that it returns False and assign that function call to the variable c_false

c_true =checkingIfIn('pine apple', direction = False)             # Call the fucntion so that it returns True and assign it to the variable c_true

fruit_ans = checkingIfIn('fruit')                                # Call the function so that the value of fruit is assigned to the variable fruit_ans

param_check = checkingIfIn('param', d = {'param':8})             # Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check

