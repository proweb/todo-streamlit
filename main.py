import streamlit as st

# Настройки окна браузера
st.set_page_config(
    page_title="TODO списочек",
    page_icon=":white_check_mark:",
    layout="centered",
    initial_sidebar_state="auto",
)

with st.sidebar:
    """
    # Python Mini-apps
    """ 
    st.page_link('main.py', label='Стартовый экран')
    st.page_link('pages/1_Crawler.py', label='Мой краулер')
    """
    --- 
    
    Простой TODO-list 
    
    на основе session value
    """
# Описание странички
"""
## Мои развлечения с питоном


мини приложения на базе Streamlit фреймворка

---
"""



if "todos" not in st.session_state:
    st.session_state['todos'] = []
else:
    st.subheader('TODO list:', anchor='todo')
    for item in st.session_state['todos']:
        st.markdown("- " + item)

# Пример формы
with st.form("formTodo", clear_on_submit=True):
    input = st.text_input(label="Добавить:", placeholder='Что надо сделать?')
    submitted = st.form_submit_button("Добавить", type="primary")

    if submitted and input:
        # Заменит значение
        st.session_state['todos'].append(input)
        st.rerun()
