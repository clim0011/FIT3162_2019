import pandas as pd

field = ['id']
a = pd.read_csv("reviews_new.csv")
b = pd.read_csv("listings_new.csv")
id_review = [0]*10248140
count = 1
# remove id that do not in reviews.csv but in listings.csv
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


newDataFrame = pd.DataFrame(columns = ['id', 'name', 'summary', 'space', 'description', 'neighborhood_overview', 'notes', 'transit', 'street', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value'])
n = 3793
m = 0
# remove row that is null
for i in range(n):
    item = id_review[b.id[i]]
    if (item != 0 and pd.isnull(b.review_scores_rating[i]) == False and pd.isnull(b.review_scores_accuracy[i]) == False and pd.isnull(b.review_scores_cleanliness[i]) == False and pd.isnull(b.review_scores_checkin[i]) == False and pd.isnull(b.review_scores_communication[i]) == False and pd.isnull(b.review_scores_location[i]) == False and pd.isnull(b.review_scores_value[i]) == False and pd.isnull(b.summary[i]) == False and pd.isnull(b.description[i]) == False and pd.isnull(b.neighborhood_overview[i]) == False and pd.isnull(b.transit[i]) == False and pd.isnull(b.notes[i]) == False and pd.isnull(b.space[i]) == False):
        newDataFrame.loc[m] = b.loc[i]
        m = m + 1

# write into listings_new_new.csv
newDataFrame.to_csv('listings_new_new.csv',index = False)

###################################################
# Use R to combine listings_new_new.csv and reviews.csv and write into MyData.csv
###################################################

c = pd.read_csv("MyData.csv")
n = 50373
m = 0
newDataFrame = pd.DataFrame(columns = ['id', 'comments', 'name', 'summary', 'space', 'description', 'neighborhood_overview', 'notes', 'transit', 'street', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value'])
# remove row that do not have comments
for i in range(n):
    if (pd.isnull(c.comments[i]) == False):
        newDataFrame.loc[m] = c.loc[i]
        m = m + 1

# write into FinalData.csv
newDataFrame.to_csv('FinalData.csv',index = False)
