# ДЗ "БИБЛИОТЕКА" ПО ТЕМЕ SQLAlchemy
Реализован вывод данных из таблиц Books и janr на главной странице, а так же добавлена возможность перехода на странницу выбранного жанра
## Запуск проекта
1) Установить виртуальное окружение 
```
   python -m venv venv  
```
3) Активировать виртуальное окружение
```
   .\venv\Scripts\activate
```
4) Устанавливаем зависимости
```
   pip install -r requirements.txt
```
5) Запуск приложения
```
    Запуск осуществляется при помощи файла app.py
    При отсутствии файла бд или тестовых данных необходимо откомментировать блок with app.app_context(): в файле app.py
```
6) Тестирование
```
    После запуска приложение осуществить переход по http://127.0.0.1:5000/ , переход по жанрам осуществляется гиперссылкой либо вручную по адресу http://127.0.0.1:5000/janr/id  "где Id - id жанра"
```