import sys
from nltk.tokenize import RegexpTokenizer
from collections import Counter

#create a list with all positive words
with open('positive-words.txt') as f:
    content_pos = f.readlines()
content_pos = [x.strip() for x in content_pos] 

#create a list with all the negative words
with open('negative-words.txt') as f:
    content_neg = f.readlines()
content_neg = [x.strip() for x in content_neg] 

#need to read in from stdout
tokenizer = RegexpTokenizer(r'\w+')

#sort headline words into negative or positive

for headline in sys.stdin:
    line=tokenizer.tokenize(headline.strip())
    words=[w.lower() for w in line]
    positiveWords = []
    negativeWords = []
    for word in words:
        if word in content_pos:
            positiveWords.append(word)    
        if word in content_neg:
            negativeWords.append(word)        
    posCount = Counter(positiveWords)
    negCount = Counter(negativeWords)
    for posWord in positiveWords:
       print posWord +','+ str(posCount[posWord])
    for negWord in negativeWords:
       print negWord+','+ str(-1 * negCount[negWord])

