import streamlit as st

st.title("Hello World!")
st.write("Welcome to my first Streamlit app.")

# Add some simple interactive elements
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")
    
st.balloons()