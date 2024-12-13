# Bishop

Choose your preferred language:

[![English](https://img.shields.io/badge/🇬🇧English-blue?style=flat-square)](./README.md)
[![Italiano](https://img.shields.io/badge/🇮🇹Italian-green?style=flat-square)](./README-it.md)
[![Polski](https://img.shields.io/badge/🇵🇱Polski-red?style=flat-square)](./README-pl.md)
[![Deutsch](https://img.shields.io/badge/🇩🇪Deutsch-yellow?style=flat-square)](./README-de.md)
[![Español](https://img.shields.io/badge/🇪🇸Espa%C3%B1ol-orange?style=flat-square)](./README-es.md)
[![Русский](https://img.shields.io/badge/🇷🇺%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-purple?style=flat-square)](./README-ru.md)

Bishop — это бот Telegram, предназначенный для отправки постов из очереди определённого сабреддита напрямую в Telegram. Пользователи могут одобрять или удалять посты с помощью простых команд.

![GitHub Repo stars](https://img.shields.io/github/stars/fen0x/Bishop?style=flat-square) 
![GitHub License](https://img.shields.io/github/license/fen0x/Bishop?style=flat-square) 

## Возможности

На данный момент Bishop поддерживает две основные команды:

- **/appost**: одобряет отправленный пост.  
- **/delrule (правило)**: удаляет пост на основании указанного правила.

Проект находится на стадии альфа и активно разрабатывается. Так как это ранняя версия, возможны ошибки или неожиданные поведения. Ваши отзывы и предложения приветствуются!

## Используемые технологии

- Язык: **Python**  
- Управление зависимостями: **Poetry**  
- Библиотеки: Telethon, PRAW  

## Начало работы

1. **Клонируйте репозиторий:**  
   ```bash
   git clone https://github.com/fen0x/Bishop.git
   cd Bishop
   ```

2. **Установите зависимости:**  
   Убедитесь, что Python и Poetry установлены, затем выполните:  
   ```bash
   poetry install
   ```

3. **Настройте бота:**  
   Отредактируйте файл `config.ini.example`, указав токен вашего Telegram-бота и другие необходимые настройки (например, сабреддит для мониторинга), и переименуйте его в `config.ini`.

4. **Запустите бота:**  
   ```bash
   poetry run python main.py
   ```

## Участие в разработке

Bishop — это проект с открытым исходным кодом. Если вы хотите принять участие:  

1. Сделайте форк репозитория.  
2. Создайте новую ветку для вашей функции или исправления.  
3. Отправьте pull request, когда работа будет завершена.  

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее в файле `LICENSE`.

---

Спасибо за интерес к Bishop! Мы надеемся на постоянное улучшение бота с помощью сообщества.