#Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
for word in str1.split():
    freq_words[word] = freq_words.get(word, 0) + 1
