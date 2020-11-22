#Now define lengths using map instead.



def lengths(strings):
    """lengths takes a list of strings as input and returns a list of numbers that are the lengths
     of strings in the input list. Use map!"""
    return list(map(lambda string : len(string), strings))

