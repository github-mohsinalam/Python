#Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017 about the S&P 500 closing prices as well as some other financial indicators,
#including the “Long Term Interest Rate”, which is interest rate paid on 10-year U.S. government bonds.

#Write a program that computes the average closing price (the second column, labeled SP500) and the highest long-term interest rate.
#Both should be computed only for the period from June 2016 through May 2017. Save the results in the variables mean_SP and max_interest.



with open('SP500.txt') as SP500:
        lines = [line.strip() for line in SP500][6:18]
        lst_SP = []
        lst_LIR = []
        for line in lines :
            items = line.split(',')
            lst_SP.append(float(items[1]))
            lst_LIR.append(float(items[5]))

        
mean_SP = sum(lst_SP)/len(lst_SP)
max_interest = max(lst_LIR)
