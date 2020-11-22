#Write a function called longlengths that returns the lengths of those strings that have at least 4 characters.
#Try it with a list comprehension.

def longlengths(strings):
    """Input is a list of strings"""
    return [len(string) for string in strings if len(string)>=4]



