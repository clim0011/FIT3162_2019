import pandas as pd

df=pd.read_csv("FinalData.csv")
print(len(df))

#Remove non-english characters
df=df[~df['comments'].str.contains(r'[^\x00-\x7F]+')]
print(len(df))

df.to_csv('FinalData.csv',index = False)

