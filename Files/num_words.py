#We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
#Find the total number of words in the file and assign this value to the variable num_words.


num_words  = 0
with open('emotion_words.txt') as emotion_words :
    for line in emotion_words:
        line = line.strip()
        num_words = num_words + len(line.split())
        

