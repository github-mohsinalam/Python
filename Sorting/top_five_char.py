#You’re going to write a function that takes a string as a parameter and returns a list of the five most frequent characters in the string.


  def top_five_char(string):
    char_dict = {}
    for char in string.strip():
        char_dict[char] = char_dict.get(char, 0) + 1
    sorted_lst = sorted(char_dict, key = lambda c :-char_dict[c])
    return sorted_lst[:5]




print(top_five_char('abggdgthhhghhsaabvb'))
