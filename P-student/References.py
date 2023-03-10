import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("My References")

content1 = """
Here comes contact information about my references 
from my different works and responsibilities.

"""
st.write(content1)

df = pandas.read_csv("../P-student/data.csv")

col1, col2 = st.columns(2)

with col1:
    for index, row in df[:1].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image(["../P-student/images/" + row["image"]], width=300)
        st.info(f'{"+"}{row["mobilenr"]}')
        st.info(row["email"])


with col2:
    for index, row in df[1:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image(["../P-student/images/" + row["image"]], width=300)
        st.info(f'{"+"}{row["mobilenr"]}')
        st.info(row["email"])




