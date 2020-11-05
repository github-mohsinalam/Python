#Write a function that reverses its string argument.


def reverse(astring):
    astring_rev = ''
    for char in astring :
        astring_rev = char + astring_rev
    return astring_rev
print(reverse('xyz'))
        
