# Smashing Wallpaper Downloader
Тестовое задание https://github.com/ostrovok-team/code-challenge/tree/master/python

Есть прекрасный сайт Smashing Magazine, который каждый месяц выкладывает отличные обои для десктопа. Заходить каждый месяц и проверять, что там нового дело не благородное, поэтому давайте попробуем автоматизировать эту задачу. Требуется написать cli утилиту, которая будет качать все обои в требуемом разрешение за указанный месяц-год в текущую директорию пользователя. Вот тут находятся все обои, а здесь находятся обои за май 2017.

# Использование

Для запуска программ требуется установленный Python </br>
В программе используются библиотеки:
* requests
* BeautifulSoup
* click

## Запуск

Для просмотра информации по использованию скрипта используется ключ `--help`

    python wall.py --help

## Аргументы

    python wall.py -m MONTH -y YEAR -c CALENDAR -s SIZE

* `-m, --month` - Требуемый месяц (по умолчанию текущий месяц).
* `-y, --year` - Требуемый год (по умолчанию текущий год).
* `-c, --cal` - Обои с календарем/без (по умолчанию с календарем).
* `-s , --size` - Требуемое разрешение в формате (ширина)x(высота) (по умолчанию 1920x1080).
* `--help` - Вызов справки.

# SQL

## 2 задание

Вам дана таблица в postgres, которая представляет из себя список сотрудников с их зарплатами и отделами. Необходимо написать запрос, который будет выбирать человека с максимальной зарплатой из каждого отдела. В качестве тестовых данных можете использовать дамп таблицы, пример схемы:

Данный запрос находится в файле `SQL(1-задание).txt`