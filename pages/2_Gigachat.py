import streamlit as st





# Настройки окна браузера
st.set_page_config(
    page_title="Gigachat AI",
    layout="centered",
    initial_sidebar_state="auto",
)

with st.sidebar:
    """
    # Python Mini-apps
    """ 
    st.page_link('main.py', label='Стартовый экран')
    st.page_link('pages/1_Crawler.py', label='Мой краулер')
    st.page_link('pages/2_Gigachat.py', label='Мой AI-помощник')
    """
    ---
    
    **AI-помощник**
    
    на освнове Gigachat
    """
    
# App title
st.title("Gigachat пример реализации")