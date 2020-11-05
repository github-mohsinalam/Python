#Write a function that removes all occurrences of a given letter from a string.



def remove_letter(theLetter, theString):
    lst_theString = list(theString)
    for i in range(lst_theString.count(theLetter)):
        lst_theString.remove(theLetter)
    newString = ''.join(lst_theString)
    return newString
print('abahca')
    

