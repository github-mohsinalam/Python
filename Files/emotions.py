#Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.


with open("emotion_words.txt") as emotion_words :
    emotions = []
    for line in emotion_words:
        line = line.strip()
        emotions.append(line.split()[0])
print(emotions)
    
