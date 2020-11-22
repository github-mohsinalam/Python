#Write a function called positives_Li_Com that receives list of things as the input and
#returns a list of only the positive things, [3, 5, 7], using the list comprehension.



things = [3, 5, -4, 7]
def positives_Li_Com(lst):
    return [x for x in lst if x>0]

print(positives_Li_Com(things))
