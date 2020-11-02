#Write a function findHypot.
#The function will be given the length of two sides of a right-angled triangle and it should return the length of the hypotenuse. 
#(Hint: x ** 0.5 will return the square root, or use sqrt from the math module)


def findHypot(a,b):
    hypotenuse = (a*a + b*b)**(0.5)
    return hypotenuse
print(findHypot(12,5))

