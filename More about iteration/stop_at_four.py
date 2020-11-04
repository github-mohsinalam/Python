#Write a function called stop_at_four that iterates through a list of numbers.
#Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.

def stop_at_four(lst):
    new_lst = []
    i = 0
    while i < len(lst) and lst[i] != 4:
        new_lst.append(lst[i])
        i = i+1
    return new_lst
# Take a list as input from the user 
my_list = list(map(int, input("Enter elements of list,each separated by space: ").strip().split()))
print(stop_at_four(my_list))
