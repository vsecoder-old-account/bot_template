<img src="https://raw.githubusercontent.com/vsecoder/bot_template/main/static/img/icon.png" width="30%">

# Bot template

## Меню

1. [Запуск](https://github.com/vsecoder/bot_template#запуск) - подробная инструкия по запуску
2. [Свойства](https://github.com/vsecoder/bot_template#свойства) - список функций со скринами
3. [TODO](https://github.com/vsecoder/bot_template#todo) - список дальнейших идей

## Запуск

```bash
git clone https://github.com/vsecoder/bot_template.git
cd bot-template
pip install -r requirements.txt
```

Замените токен телеграмм бота в файле bot.py на свой и запустите:

```bash
python bot.py
```

Всё, теперь вы можете из данного шаблона писать других ботов, админка за вас уже есть)))

## Свойства:

***Интерфейс:***

![img1](https://raw.githubusercontent.com/vsecoder/bot_template/main/md/image_1.png)

***Таблица юзеров с поиском:***

![img2](https://raw.githubusercontent.com/vsecoder/bot_template/main/md/image_2.png)

![img3](https://raw.githubusercontent.com/vsecoder/bot_template/main/md/image_3.png)

***Публикация рекламы с поддержкой html и emoji:***

![img4](https://raw.githubusercontent.com/vsecoder/bot_template/main/md/image_4.png)

***Система логирования в файлы:***

![img5](https://raw.githubusercontent.com/vsecoder/bot_template/main/md/image_5.png)

## TODO:

1. Заменить flask на ассинхроную библиотеку aiohttp

2. Расширить возможности отправки рекламы

3. Сделать защиту админки паролем
