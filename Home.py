import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
import pandas

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Parsova Khayatan")
    content = """
    I am a junior Python programmer, worked +20 years in IT/Telecom. 
    Newly, I am working to deepen my Devops knowledge and expertise. 
    Including CI/CD, Jenkins, Maden, Jason, AWS, Git, ...
    """
    st.info(content)

content2 = """
Below you can find some of the apps I've built in Python. Feel free to contact me!
"""
st.write(content2)

df = pandas.read_csv("data.csv", sep=";")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(["images/" + row["image"]])
#        st.write("[Source Code](https://pythonhow.com)")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(["images/" + row["image"]])
#        st.write("[Source Code](https://pythonhow.com)")
        st.write(f"[Source Code]({row['url']})")