import pandas as pd
from nltk.corpus import stopwords
from rake_nltk import Rake
import operator

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

#output top 100 
for i in range(100):
    print(x[i])
