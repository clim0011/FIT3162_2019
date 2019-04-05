import pandas as pd
from nltk.corpus import stopwords
from rake_nltk import Rake
import operator
import nltk
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

#our dataset
df = pd.read_csv("FinalData.csv")
stopWords = set(stopwords.words('english'))
#print(stopWords)
#remove "not" from stopword
#stopWords.remove("not")

r=Rake(stopwords=stopWords)
aList=[]
#dictionary to keep our keyword and frequency
keyword={}

#extract keywords
for i in range(len(df["comments"])):
    r.extract_keywords_from_text(df["comments"][i])
    aList.append(r.get_ranked_phrases())

#compute frequency
#insert into the dictionary
#key: keyword, value: frequency
for i in range(len(aList)):
    for k in range(len(aList[i])):
        if aList[i]!=[]:
            if aList[i][k] in keyword:
                keyword[aList[i][k]]+=1
            else:
                keyword[aList[i][k]]=1

#sort the dictionary based on frequency
x=sorted(keyword.items(), key=operator.itemgetter(1), reverse=True)
#number of keywords
print(len(x))

#combine synonyms
#nltk.download('wordnet')
#nltk.download('stopwords')
for i in range(len(keyword)):
    word=x[i][0]    #keyword to go through
    synonyms=[]     #to store the synonyms of the current keyword
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    synonyms=set(synonyms)
    #loop through the keywords to check if there is any synonyms
    for k in range(len(x)):
        currentword=x[k][0]
        if currentword in synonyms and currentword!=word:
            keyword[word]+=keyword[currentword] #combine the frequency
            del keyword[currentword]    #remove the keyword from dictionary
            x.remove(x[k])              #and from the list of keywords
        if len(x)==k+1:     #checked all the keywords
            break
    if len(keyword)==i+1:
        break

#sort the dictionary based on frequency
x=sorted(keyword.items(), key=operator.itemgetter(1), reverse=True)

#output top 100 
for i in range(100):
    print(x[i])
"""
words = ["spacing"]
ps = PorterStemmer()
 
for word in words:
    print(ps.stem(word))
"""
