Телеграмм бот позволяет найти выгодное предложение на платформе [Hotels.com](https://hotels.com/).
Пользователь с помощью специальных команд бота может выполнить следующие действия (получить следующую информацию):
- Узнать топ самых дешёвых отелей в городе (**команда /lowprice**). 
- Узнать топ самых дорогих отелей в городе (**команда /highprice**). 
- Узнать топ отелей, наиболее подходящих по цене и расположению от центра (самые дешёвые и находятся ближе всего к центру) (**команда /bestdeal**). 
- Узнать историю поиска отелей (**команда /history**)

## Запуск проекта (на примере Windows)

 - Склонируйте репозиторий в папку проекта https://github.com/ArtyomBatmanov/Hotels-bot.git
 - Установите необходимые библиотеки командой "pip install -r requirements.txt"
 - Создайте файл .env по шаблону .env.template
 - Запустите бота командой "python main.py"

## Описание работы команд

### Команда /start

После ввода команды: 
1. Выводится приветствие пользователю

### Команда /help

После ввода команды: 
1. Выводится список всех команд, кратким описанием что делает каждая команда


### Команда /lowprice

После ввода команды у пользователя запрашивается: 
1. Город, где будет проводиться поиск
2. Выдается список возможных вариантов городов в виде inline-клавиатуры, пользователь выбирает нужный
3. Количество отелей, которые необходимо вывести в результате (не больше заранее определённого максимума)
4. Запрашиваются минимальная и максимальная стоимость отеля в долларах США
5. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий (не больше заранее определённого максимума)
6. Выводится календарь с возможностью выбора даты заезда или выезда. 

### Команда /highprice 

После ввода команды у пользователя запрашивается: 
1. Город, где будет проводиться поиск
2. Выдается список возможных вариантов городов в виде inline-клавиатуры, пользователь выбирает нужный
3. Количество отелей, которые необходимо вывести в результате (не больше заранее определённого максимума)
4. Запрашиваются минимальная и максимальная стоимость отеля в долларах США
5. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий (не больше заранее определённого максимума)
6. Выводится календарь с возможностью выбора даты заезда или выезда. 

### Команда /bestdeal

После ввода команды у пользователя запрашивается: 
1. Город, где будет проводиться поиск
2. Выдается список возможных вариантов городов в виде inline-клавиатуры, пользователь выбирает нужный
3. Количество отелей, которые необходимо вывести в результате (не больше заранее определённого максимума)
4. Запрашиваются минимальная и максимальная стоимость отеля в долларах США
5. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий (не больше заранее определённого максимума)
6. Выводится календарь с возможностью выбора даты заезда или выезда. 
7. Диапазон расстояния, на котором находится отель от центра

### Команда /history

После ввода команды пользователю выводится история поиска отелей: 
1. Выдает список выполненных пользователем запросом, но не более 5
2. Дату и время ввода команды
3. То слово (город), по которому пользователь искал отели
4. Если пользователю фотографии были не нужны, то они выведены не будут


## Описание внешнего вида и UI
Окно Telegram-бота при запущенном Python-скрипте воспринимает следующие команды:
- /start - запуск бота
- /help — помощь по командам бота 
- /lowprice — вывод самых дешёвых отелей в городе
- /highprice — вывод самых дорогих отелей в городе 
- /bestdeal — вывод отелей, наиболее подходящих по цене и расположению от центра
- /history — вывод истории поиска отелей