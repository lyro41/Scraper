## Цели

Наша цель - научить структурировать код в питоновских проектах, а также узнать, как устроена веб-страница.

## Задание

Задача скрапера - добыть данные с веб-страниц. Такой подход нужен только тогда, когда у поставщика данных нет какого-то установленного протокола скачивания данных или доступа к хранилищу данных (или всё это стоит денег, которые не вписываются в наш бюджет =) ). Логику выполнения этой задачи можно разделить на три модуля:

1. Модуль, который скачивает код веб-страницы на компьютер, чтобы обрабатывать данные с нее локально;
2. Модуль, который найдет и структурирует данные в исходном коде веб-страницы;
3. Модуль, который обрабатывает данные в соответствии с бизнес-логикой системы.

Также нам нужна точка входа в наше приложение - то место, где будет собран весь основной функционал, который мы хотим сделать доступным пользователем нашего модуля.

Наш проект небольшой - поэтому нам понадобится всего 4 файла для описания вышеперечисленных модулей. Ваша задача - написать эти 4 файла с кодом, где, соответственно, будет описана логика каждого подмодуля:

1. `download.py` - модуль, ответственный за скачивание веб-страницы. Содержит описание класса Downloader (см. блокнот с заданием).
2. `parse.py` - модуль, в котором описана логика выделения данных из исходного кода веб-страницы. Содержит описание класса Parser (см. блокнот с заданием). Рекомендуется для парсинга веб-страницы использовать библиотеку BeautifulSoup4.
3. `data.py` - модуль, в котором описана любая логика обработки полученных и структурированных файлов (на ваш выбор).
4. `__init__.py` - файл, в котором будет описана функция process, которая будет принимать на вход адрес страницы, которую мы хотим заскрапить, опциональным аргументом путь к файлу, который будет хранить копию страницы на локальном компьютере, и еще одним опциональным аргументом - путь к файлу, куда мы сохраним результаты парсинга страницы. Возвращать эта функция должна результат исполнения какой-то части логики, описанной в data.py.

## Сдача работы и проверка

Вам нужно загрузить в GIT в папку `src` папку с файлами `download.py`, `parse.py`, `data.py`, `__init__.py`, в которых будет описан код скрапера.  


