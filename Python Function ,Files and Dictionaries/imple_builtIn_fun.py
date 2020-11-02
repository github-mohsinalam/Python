#Although Python provides us with many list methods,
#it is good practice and very instructive to think about how they are implemented. 
#Implement a Python function that works like the following:
# count
#in
#reverse
#index
#insert


# Implemention of COUNT
def is_count(item, sequence):
    count = 0
    for char in sequence :
        if char == item :
            count = count + 1
    return count

# Implemention of  in
def is_in(item, sequence):
    for char in sequence :
        if char == item:
            return True
    return False
 
 #Implemention of reverse
def reverse(sequence):
    rev_seq = []
    for char in sequence :
        rev_seq = [char] + rev_seq
    return rev_seq

#Implemention of index
def position(item, sequence):
    for pos, char in enumerate(sequence) :
        if char == item :
            return pos
    return 'Item not present.'
 
 #Implemention of insert
def will_insert(pos, item, lst):
    return lst[:pos] + [item] + lst[pos:]

mylst = [1,5,6]
newlist = will_insert(2,999, mylst)
print(newlist)
print(mylst)
