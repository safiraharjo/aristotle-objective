def subjectivity(df,column_no,TextBlob):
    subj = []

    for i in range(len(df)):
        item = TextBlob(df.iloc[i, column_no]).subjectivity
        subj.append(item)
    
    df['subjectivity'] = subj

    return df