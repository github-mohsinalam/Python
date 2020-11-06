#Define a function called nums that has three parameters. The first parameter, an integer, should be required.
#A second parameter named mult_int should be optional with a default value of 5. 
#The final parameter, switch, should also be optional with a default value of False. 
#The function should multiply the two integers together, 
#and if switch is True, should change the sign of the product before returning it.



def nums(x, mult_int = 5, switch = False):
    product = x*mult_int
    if switch == True:
        return -product
    else :
        return product
    
