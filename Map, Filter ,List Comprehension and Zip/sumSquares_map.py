#Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.
#Try it using map and sum.


def sumSquares(L):
    return sum(list(map(lambda x : x**2, L)))

nums = [3, 2, 2, -1, 1]

print(sumSquares(nums))
