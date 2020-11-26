#Write a program that allows the user to enter a string.
#It then prints a table of the letters of the alphabet in
#alphabetical order which occur in the string together with the number of times each letter occurs.


text = input('Enter a string: ').lower()
dic = {}
for char in text :
    if char.isalpha() == True:        #char.isalpha() return True if char is a  letter of English alphabet.
        dic[char] = dic.get(char, 0) + 1
for k in sorted(dic):
    print(k , dic[k])
    
