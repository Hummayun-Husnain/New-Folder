import streamlit as st
def clean_text(text):
    text = text.replace("'","").replace("-\n","").replace("\n"," ").strip()
    return (text)
st.title('Intro to Layout and Images:')
st.sidebar.image("download.jpg",width=100)
st.sidebar.header('Options')
text = st.sidebar.text_area("Paste Your Text")
button1 = st.sidebar.button("Clean Text")
if button1:
    col1,col2 = st.beta_columns(2)
    col1_expender = col1.beta_expender('Extend Text')
    with col1_expender:
        col1_expender.header("OriginalText")
        col1_expender.write(text)
    col2_expender = col2.beta_expender('Extend Text')
    with col2_expender:
        col2_expender.header("Clean Text")
        col2_expender.write(text)
