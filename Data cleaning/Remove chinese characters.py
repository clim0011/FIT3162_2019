import pandas as pd

df=pd.read_csv("FinalData.csv")

#Remove non-english characters
df['comments'] = df['comments'].str.replace(r'[^\x00-\x7F]+', '')

df.to_csv('FinalData.csv',index = False)

