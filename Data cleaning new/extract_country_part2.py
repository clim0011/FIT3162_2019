Netherlands_df_2 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Kingdom_df_2 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
France_df_2 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Spain_df_2 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Italy_df_2 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])
Austria_df_2 = pd.DataFrame(columns = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Average_Score', 'Hotel_Name', 'Reviewer_Nationality', 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Positive_Review', 'Review_Total_Positive_Word_Counts', 'Reviewer_Score', 'Tags'])

n_n_2 = 0
n_k_2 = 0
n_f_2 = 0
n_s_2 = 0
n_i_2 = 0
n_a_2 = 0

for i in range (100000,200000):
    print(i)
    item_location = a.Hotel_Address[i].rsplit(' ', 1)[-1]
    item_tag = a.Tags[i].split()
    
    if item_tag[1] == "Leisure" and item_location == "Netherlands":
        Netherlands_df_2.loc[n_n_2] = a.loc[i]
        n_n_2 = n_n_2 + 1
    elif item_tag[1] == "Business" and item_location == "Netherlands":
        Netherlands_df_2.loc[n_n_2] = a.loc[i]
        n_n_2 = n_n_2 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "Kingdom":
        Kingdom_df_2.loc[n_k_2] = a.loc[i]
        n_k_2 = n_k_2 + 1
    elif item_tag[1] == "Business" and item_location == "Kingdom":
        Kingdom_df_2.loc[n_k_2] = a.loc[i]
        n_k_2 = n_k_2 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "France":
        France_df_2.loc[n_f_2] = a.loc[i]
        n_f_2 = n_f_2 + 1
    elif item_tag[1] == "Business" and item_location == "France":
        France_df_2.loc[n_f_2] = a.loc[i]
        n_f_2 = n_f_2 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "Spain":
        Spain_df_2.loc[n_s_2] = a.loc[i]
        n_s_2 = n_s_2 + 1
    elif item_tag[1] == "Business" and item_location == "Spain":
        Spain_df_2.loc[n_s_2] = a.loc[i]
        n_s_2 = n_s_2 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "Italy":
        Italy_df_2.loc[n_i_2] = a.loc[i]
        n_i_2 = n_i_2 + 1
    elif item_tag[1] == "Business" and item_location == "Italy":
        Italy_df_2.loc[n_i_2] = a.loc[i]
        n_i_2 = n_i_2 + 1
        
        
    elif item_tag[1] == "Leisure" and item_location == "Austria":
        Austria_df_2.loc[n_a_2] = a.loc[i]
        n_a_2 = n_a_2 + 1
    elif item_tag[1] == "Business" and item_location == "Austria":
        Austria_df_2.loc[n_a_2] = a.loc[i]
        n_a_2 = n_a_2 + 1
