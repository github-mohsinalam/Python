#Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen.
#Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.



p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

low_d = {}
for c in p:
    c=c.lower()
    low_d[c] = low_d.get(c,0)+1
