#Below, we have provided a nested list called big_list.
#Use nested iteration to create a dictionary, word_counts, that contains all the words in big_list as keys, and the number of times they occur as value.



big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]

word_counts = {}
for lst1 in big_list:
    for lst2 in lst1:
        for item in lst2:
            word_counts[item] = word_counts.get(item,0)+1
            
