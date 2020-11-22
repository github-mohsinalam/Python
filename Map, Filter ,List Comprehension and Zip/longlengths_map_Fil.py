#Write a function called longlengths that returns the lengths of those strings that have at least 4 characters.
#Try it using map and filter.


def longlengths(strings):
    '''input is a list of strings'''
    return list(map(len, filter(lambda string : len(string)>=4, strings)))



