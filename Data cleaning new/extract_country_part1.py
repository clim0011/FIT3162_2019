Netherlands_df_1 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Kingdom_df_1 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
France_df_1 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Spain_df_1 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Italy_df_1 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Austria_df_1 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])

n_n_1 = 0
n_k_1 = 0
n_f_1 = 0
n_s_1 = 0
n_i_1 = 0
n_a_1 = 0

for i in range (0,100000):
    print(i)
    item_location = a.Hotel_Address[i].rsplit(' ', 1)[-1]
    item_tag = a.Tags[i].split()
    
    if item_tag[1] == "Leisure" and item_location == "Netherlands":
        Netherlands_df_1.loc[n_n_1] = a.loc[i]
        n_n_1 = n_n_1 + 1
    elif item_tag[1] == "Business" and item_location == "Netherlands":
        Netherlands_df_1.loc[n_n_1] = a.loc[i]
        n_n_1 = n_n_1 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "Kingdom":
        Kingdom_df_1.loc[n_k_1] = a.loc[i]
        n_k_1 = n_k_1 + 1
    elif item_tag[1] == "Business" and item_location == "Kingdom":
        Kingdom_df_1.loc[n_k_1] = a.loc[i]
        n_k_1 = n_k_1 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "France":
        France_df_1.loc[n_f_1] = a.loc[i]
        n_f_1 = n_f_1 + 1
    elif item_tag[1] == "Business" and item_location == "France":
        France_df_1.loc[n_f_1] = a.loc[i]
        n_f_1 = n_f_1 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "Spain":
        Spain_df_1.loc[n_s_1] = a.loc[i]
        n_s_1 = n_s_1 + 1
    elif item_tag[1] == "Business" and item_location == "Spain":
        Spain_df_1.loc[n_s_1] = a.loc[i]
        n_s_1 = n_s_1 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "Italy":
        Italy_df_1.loc[n_i_1] = a.loc[i]
        n_i_1 = n_i_1 + 1
    elif item_tag[1] == "Business" and item_location == "Italy":
        Italy_df_1.loc[n_i_1] = a.loc[i]
        n_i_1 = n_i_1 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "Austria":
        Austria_df_1.loc[n_a_1] = a.loc[i]
        n_a_1 = n_a_1 + 1
    elif item_tag[1] == "Business" and item_location == "Austria":
        Austria_df_1.loc[n_a_1] = a.loc[i]
        n_a_1 = n_a_1 + 1        
