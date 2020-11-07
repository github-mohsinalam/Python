#sort the list nums based on the last digit of each number from highest to lowest



nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums, reverse = True, key = lambda s:s[-1])
print(numns_sorted_lambda)
