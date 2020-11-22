#Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.
#Try it using an accumulator pattern.



def sumSquares(L):
    sum_suq = 0
    for n in L :
        sum_suq += n*n
    return sum_suq
    

nums = [3, 2, 2, -1, 1]
print(sumSquares(nums))


