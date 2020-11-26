#Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”.


with open("emotion_words.txt") as emotion_words:
    j_emotions = []
    for line in emotion_words:
        for word in line.split() :
            if word[0] == "j":
                j_emotions.append(word)
print(j_emotions) 
                
                                

    
