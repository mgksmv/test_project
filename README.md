# Тестовое задание web-программист (Python)

Суть задания: нужно разработать таблицу в формате Single Page Application.
<br>
<br>

Чтобы начать, скачайте все необходимые зависимости с requirements.txt:

```
pip install -r requirements.txt
```

<br>
Затем подставьте свои данные базы данных:
<br>
<br>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # я использовал MySQL. Можно и заменить на другую, но придется удалить драйвер MySQL, который скачался с requirements.txt
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}
```

<br>
Затем стандартные команды для миграции таблиц в базу данных:
<br>
<br>

```
python manage.py makemigrations
```
```
python manage.py migrate
```

<br>
Далее сгенерируем случайные (фейковые) данные в базу данных.<br>
Данный код сгенерирует 100 случайных данных (можно указать любое число):
<br>
<br>

```
python manage.py faker 100
```

<br>
Теперь можно запустить сервер:
<br>
<br>

```
python manage.py runserver
```