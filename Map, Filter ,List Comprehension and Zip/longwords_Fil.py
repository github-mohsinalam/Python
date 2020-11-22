#Define longewords using filter




def longwords_Fil(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use the filter function."""
    
    return list(filter(lambda string : len(string)>4 , strings))

