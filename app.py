import streamlit as st
st.title("Hello world")

age=st.slider("how are you",0,130,25)
st.write("i m",age,"years old")

brothers_age=st.slider("how old is your brother",0,130,25)
st.write("my brother is",age,"years old")

c=age+brothers_age
st.write("sum of age is",c)