import streamlit as st


# Настройки окна браузера
st.set_page_config(
    page_title="Онлайн-помощник",
    page_icon=":tomato:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={'About': "Пример приложения от Сереги"}
)

# Инициализация списка сообщений
if "messages" not in st.session_state:
    st.session_state.messages = []


# Отображение всех сообщений
st.title("Задачки на сегодня:")
for msg in st.session_state.messages:
    st.write(f"**{msg['name']}:** {msg['message']}")
    st.divider()


st.write("---")

# Заголовок приложения
st.header("Что сделать хозяин надо?")

# Форма для ввода данных
with st.form("guestbook_form"):
    name = st.text_input("Задача")
    message = st.text_area("Примечание")
    submitted = st.form_submit_button("Старт")

    if submitted and name and message:
        # Добавление нового сообщения
        st.session_state.messages.append({"name": name, "message": message})



