#Write a function called positives_Acc that receives list of numbers as the input (like [3, -1, 5, 7]) and
#returns a list of only the positive numbers, [3, 5, 7], via manual accumulation.


def positives_Acc (lst):
    pos_lst = []
    for x in lst:
        if x>0:
            pos_lst.append(x)
    return pos_lst
        

