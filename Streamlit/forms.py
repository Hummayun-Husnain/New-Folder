import streamlit as st
import spacy
st.cache(allow_output_mutation=True)
def model_load(model):
    nlp = spacy.load(model)
nlp = model_load('en_core_web_lg')
def extract_entity(ent_type,text):
    results=[]
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ent_type:
            results.append((ent.text, ent.label_))
    return (results)
st.title('Forms in streamlit:')
form1=st.sidebar.form(key="Option")
form1.header('Parameters')
ent_types = form1.multiselect('Select entities you want to select',['Person','ORG','GPE'])
form1.form_submit_button()
text = st.text_area('Sample Text','Ali enjoys playing football in Flourida for the Salvation Army')
hits = extract_entity(ent_types,text)
st.write(hits)