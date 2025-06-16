# Project

Первое приложение на Python Streamlit

```
uv --version
```

```
uv init myapp
cd myapp
```

```
uv add streamlit
```

```
.venv\Scripts\activate
```




запустить проект
```
streamlit run .\main.py
```


Выгрузка зависимостей 
```
uv pip freeze > requirements.txt
```

Обновить пакеты
```
uv pip install --upgrade streamlit
```

или попробовать
```
uv lock --upgrade
uv sync
```