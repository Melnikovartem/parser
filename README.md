# parser
Small summer project, that can probably help if i put some time into it after

## Helpful commands

Using flask cli to boot everything up

Migration:

```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
```

Server boot (from main folder):

```bash
$ export FLASK_APP=server
$ flask run
```


## What is this about (rus.)

Агрегируем данные отзывов на товары с разных маркетплейсов. В рамках мини-проекта использую только 1 сайт тк тучу времени убил на налаживание Flask + бд. Также пока получил не везде доступ / к каждому маркетплейсу нужен свой подход (у кого api, у кого через js показываются отзывы, так что пока самая базовая версия готова).

## Some thoughts

У меня есть лист TODO, который пополняется каждый раз, как сажусь подумать, что хотелось бы сделать еще до рабочей версии. Так что, если будут коммиты после дедлайна, то спокойно откатывайтесь до коммитов ~18 23:59 (я там еще час убил на то, что записывал + красивые странички на jninja писал, но концептуально основной парсинг и сохранение данных имеется к дедлайну)
