#Write a function that mirrors its string argument, 
#generating a string containing the original string and the string backwards.


def reverse(astring):
    astring_rev = ''
    for char in astring :
        astring_rev = char + astring_rev
    return astring_rev
def mirror(mystr):
    return mystr+reverse(mystr)
print(mirror('good'))
    
