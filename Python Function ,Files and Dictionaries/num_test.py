#Write a function named num_test that takes a number as input. 
#If the number is greater than 10, the function should return “Greater than 10.” 
#If the number is less than 10, the function should return “Less than 10.” 
#If the number is equal to 10, the function should return “Equal to 10.”

def num_test(number):
    if number > 10:
        return 'Greater than 10.'
    elif number < 10:
        return 'Less than 10.'
    else:
        return 'Equal to 10.'

print(num_test(15))
print(num_test(7))
    
   

