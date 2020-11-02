Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. 
#Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.

#Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. 
#If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as
#if  abs(x - y) < 0.001:       


def is_rightangled(a, b, c):
    y = (a*a + b*b)**(0.5)
    if abs(c-y) < 0.0001:         # checking if c is approximately equal to y
        return True 
    else :
        return False
    
        
print(is_rightangled(4.1,8.2,9.168))
 


