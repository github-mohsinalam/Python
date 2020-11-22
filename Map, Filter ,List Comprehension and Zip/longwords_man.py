#Define longwords using manual accumulation.

def longwords(strings):
    """Return a shorter list of strings containing only the strings with more than four characters. Use manual accumulation."""
    
    lst4 = []
    for string in strings:
        if len(string)>4:
            lst4.append(string)
    return lst4

