#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for c in str1:
    freq[c] = freq.get(c,0) + 1
