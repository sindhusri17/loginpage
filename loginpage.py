import streamlit as st
st.title("LOGIN PAGE")

user=st.text_input("ENTER USER NAME")
pwd=st.text_input("PASSWORD",type="password")

def login():
    if user=='admin' and pwd=="1234":
        st.success("valid user")
        st.balloons()
        st.link_button("st.peter's","https://www.spechyd.ac.in/")
    else:
        st.error("INVALID USER")
st.button("LOGIN",on_click=login)
