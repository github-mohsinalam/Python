#Write a program that finds the most used 7 letter word in scarlet3.txt.

dic = {}
with open('scarlet3.txt', 'r')as text :
    for line in text :
        line = line.strip()
        words = line.split()
        for word in words:
            dic[word] = dic.get(word, 0) + 1
    most_used = list(dic.keys())[0]
    for k in dic :
        if len(k) == 7:
            if dic[k] > dic[most_used]:
                most_used = k
print(most_used, dic[most_used])
          
        
