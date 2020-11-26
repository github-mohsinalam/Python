#Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.


pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['restaurant'] = 'galley'
pirate['madam'] = 'proud beauty'
pirate['professor'] = 'foul blaggart'
pirate['restaurant'] = 'galley'
pirate['your'] = 'yer'
pirate['excuse'] = 'arr'
pirate['students'] = 'swabbies'
pirate['are'] = 'be'
pirate['lawyer'] = 'foul blaggart'
pirate['the'] = 'th'
pirate['restroom'] = 'head'
pirate['my'] = 'me'
pirate['hello'] = 'avast'
pirate['is'] = 'be'
pirate['man'] = 'matey'
translation = []
sentence = input('Enter a sentence in English')
words = sentence.split()
for word in words :
    if word in pirate:
        translation.append(pirate[word])
    else:
        translation.append(word)
print(' '.join(translation))
        
        
