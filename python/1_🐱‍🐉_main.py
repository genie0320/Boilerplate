import streamlit as st

st.set_page_config(
    page_title="My Langchain journey.",
    page_icon="😍"
)

st.title('Hello, Beauty!')
st.sidebar.success('Menus')


st.session_state['test'] = st.text_input('input')


st.write("DB username:", st.secrets["TEST_KEY"])
