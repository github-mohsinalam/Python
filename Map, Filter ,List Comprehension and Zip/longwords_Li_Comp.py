#Define longewords using filter


def longwords_Li_Comp(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use a list comprehension."""
    return [string for string in strings if len(string)>4 ]

