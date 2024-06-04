"""
Streamlit:
	Streamlit is a python library to create web apps for data science and machine learning.
How to run program:
	open command prompt in the folder of file and type: streamlit run [file name]
"""

import streamlit as st
st.title('Streamlit Tutorial App')
st.write('This is my first try.')
button1=st.button('Click Me')
if button1:
    st.write('You clicked the button')

st.header('Checkbox Section')
like = st.checkbox('Do you like it?')
button2 = st.button('Submit!')
if button2:
    if like:
        st.write('Thank You')
    else:
        st.write('Sorry')

st.header('Radio Button Section')
animal = st.radio('What animal do you like?',('Lion','Bear','Zebra','Non of Above'))
button3=st.button('Submit')
if button3:
    st.write(animal)
    if animal == 'Lion':
        st.write('ROAR!')

st.header('Select box Section')
animal2 = st.selectbox('What animal do you like?',('Lion','Bear','Zebra','Non of Above'))
button4=st.button('Submit animal')
if button4:
    st.write(animal2)
    if animal2 == 'Lion':
        st.write('ROAR!')

st.header('Multiselect Section')
option= st.multiselect('What animal do you like?',['Lion','Bear','Zebra','Non of Above'])
button5=st.button('Print animal')
if button5:
    st.write(option)

st.header('Slider Section')
num = st.slider('How many epochs?',1,100,10)
if st.button('Slider Clicked'):
    st.write(num)

st.header('Text input Section')
user_text = st.text_input("What's your favourite movie?",'Avengers')
if st.button('Text Button'):
    st.write(user_text)
txt = st.text_area('Reviews','''This movie was awful! The acting was terrible, and the plot was nonsensica.
I laughed so hard during this movie! It was hilarious and heartwarming.
The special effects were amazing, but the story was a bit predictable.''')
user_num = st.number_input("What's your favourite number?")
if st.button('Number Button'):
    st.write(user_num)
