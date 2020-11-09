#Write code to rearrange the strings in the list winners so that they are in alphabetical order by first name from A to Z.



winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']


def fun_key(string):
    names = string.split()
    first_name = names[0]
    return first_name


winners = sorted(winners, key = fun_key)

