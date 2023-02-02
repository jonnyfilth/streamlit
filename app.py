import streamlit as st

with st.sidebar:
    btn_hello = st.button('Clique aqui')
    btn_clear = st.button('Limpar')

info = st.empty()

if btn_hello:
    info.success('Olá Mundo')

if btn_clear:
    info.empty()