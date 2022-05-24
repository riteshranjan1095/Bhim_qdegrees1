import pandas as pd
import streamlit as st
import pandas as pd
st.title('Qdegrees')
st.header('Free text automation ')
st.select_slider()


option = st.selectbox(
     'NPS category',
     ('Bhim', 'Girnar', 'ICICI'))

st.write('You selected:', option)

# st.button('Upload excel/csv file')
st.file_uploader('upload a fill uploader file')

