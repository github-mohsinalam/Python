#Write code to switch the order of the winners list so that it is now A to Z by last name. Assign this list to the variable z_winners.


winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']



def fun_key(string):
    names = string.split()
    last_name = names[-1]
    return last_name



z_winners = sorted(winners, key = fun_key)
