#Write code to switch the order of the winners list so that it is now Z to A, by first name. Assign this list to the variable z_winners.


winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']



def fun_key(string):
    names = string.split()
    first_name = names[0]
    return first_name



z_winners = sorted(winners, key = fun_key, reverse = True)
