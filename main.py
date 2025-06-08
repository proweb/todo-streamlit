import streamlit as st


# Настройки окна браузера
st.set_page_config(
    page_title="Онлайн-помощник",
    page_icon=":tomato:",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.sidebar.write("""
# TODO :tomato:
            
Храним данные в сессии в виде List
""" )


if "item" not in st.session_state:
    st.session_state.item = []



 
st.subheader('Вывод ДО формы')
st.caption("Хранилище сессии")
st.write(st.session_state)


# Заголовок приложения
st.subheader("Форма для добавления?")

# Пример формы
with st.form("formTodo", clear_on_submit=True):
    input = st.text_input(label="Задача на сегодня:", placeholder='Что надо сделать?')
    submitted = st.form_submit_button("Submit", type="primary")

    if submitted and input:
        # Заменит значение
        st.session_state.item.append(input)
        st.rerun()



st.subheader('Вывод после формы')
st.caption("То что ввели")
st.write(input)
st.caption("st.session_state.item")
st.write(st.session_state)
st.caption("Отправлена форма или нет")
st.write(submitted)