"""
Session State is a way to share variables between reruns, for each user session.
"""
import streamlit as st
container = st.beta_container()
if "counter" not in st.session_state:
    st.session_state.counter=0
st.write(st.session_state.counter)
if st.button("Up"):
    st.session_state.counter+=1
    container.write(st.session_state.counter)
if st.button("Reset"):
    st.session_state.counter=0
