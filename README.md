# Обрезка ссылок с помощью Битли

* Принимает на вход URL пользователя и сокращает его.
* Если на вход передаётся __сокращённый URL__, возвращает количество переходов по этому адресу.

## Как установить


- Создайте файл  `.env`  в корневой директории рядом с  `main.py` .
- В файл  `.env`  добавьте строку со значением:

`TOKEN_BITLY=Ваш токен`

Чтобы получить, токен необходимо завести аккаунт на сайте - https://app.bitly.com/settings/api/

## Требования к окружению

Python3 должен быть уже установлен.
Затем используйте  pip  (или  pip3 , есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
