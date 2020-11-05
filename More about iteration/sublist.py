#Write a function, sublist, that takes in a list of numbers as the parameter. 
#In the function, use a while loop to return a sublist of the input list. 
#The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).


def sublist(lst):
    i = 0
    sub_lst = []
    while i< len(lst) and lst[i] != 5:
        sub_lst.append(lst[i])
        i = i+1
    return sub_lst

print(sublist([1,6,7,9,3,5,6,8]))       
        


