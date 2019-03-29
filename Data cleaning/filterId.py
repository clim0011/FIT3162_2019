import pandas as pd

field = ['id']
a = pd.read_csv("reviews_new.csv")
b = pd.read_csv("listings_new.csv")
id_review = [0]*10248140
count = 1
for i in range(84848):
    if (a.id[i] == a.id[i+1]):
        count = count + 1
    else:
        id_review[a.id[i]] = count
        count = 1
if (a.id[84847] != a.id[84848]):
    id_review[a.id[84848]] = 1
else:
    id_review[a.id[84848]] = count
