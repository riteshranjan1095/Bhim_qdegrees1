import streamlit as st

import pandas as pd
import numpy as np

import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
import string
from nltk import PorterStemmer
from io import BytesIO
from nltk.sentiment.vader import SentimentIntensityAnalyzer

ps =PorterStemmer()
Senti = SentimentIntensityAnalyzer()

# Sentiment code

def sentiment_cal(text):
    sentence =text

    dic = Senti.polarity_scores(sentence)
    if dic['compound']>0:
        return 'Postive'
    elif dic['compound']<0:
        return 'Negative'
    else :
        return 'Neutral'

# Cleaning code

def clean_text(text):
    delete_dict = {sp_character: '' for sp_character in string.punctuation}
    delete_dict[' '] = ' '
    table = str.maketrans(delete_dict)
    text1 = text.translate(table)

    textArr = text1.split()
    text2 = ' '.join([w for w in textArr if (not w.isdigit() and (not w.isdigit() and len(w) > 1))])
    return text2.lower()

# excel conversion code

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    format1 = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', None, format1)
    writer.save()
    processed_data = output.getvalue()
    return processed_data

st.title('CALCULATE SENTIMENT OF CUSTOMER VOCs')
st.header("Upload excel sheet with Column name 'FREE TEXT'")

uploaded_file = st.file_uploader("Choose a file")
df =pd.read_excel(uploaded_file)
df= df.astype(str)




if st.button('CALCULATE SENTIMENT'):
    df['Cleaned_Remarks']=''
    df['Cleaned_Remarks']= df['Free text'].apply(clean_text)
    df['Sentiment']=df['Cleaned_Remarks'].apply(sentiment_cal)
    df_xlsx = to_excel(df)
    st.download_button(
        label="Download data as CSV",
        data=df_xlsx,
        file_name='large_df.csv',
        mime='text/csv',
    )
