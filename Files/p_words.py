#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.



with open("school_prompt.txt") as school_prompt:
    p_words = []
    for line in school_prompt :
        line = line.strip()
        words = line.split()
        for word in words:
            if "p" in word :
                p_words.append(word)
print(p_words)
        
