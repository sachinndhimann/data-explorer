import streamlit as st
import pandas as pd
import base64
import io

vals= ['A','B','C']
df= pd.DataFrame(vals, columns=["Title"])
df

towrite = io.BytesIO()
downloaded_file = df.to_excel(towrite, encoding='utf-8', index=False, header=True)
print("Type,",type(downloaded_file))

towrite.seek(0)  # reset pointer
b64 = base64.b64encode(towrite.read()).decode()  # some strings
linko= f'<a href="data:application/vnd.openxmlformats
-officedocument.spreadsheetml.sheet;base64,{b64}"
  download="myfilename.xlsx">Download excel file</a>'
st.markdown(linko, unsafe_allow_html=True)