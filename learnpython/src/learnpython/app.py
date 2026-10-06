"""
Приложение для изучения Python — версия 2.0
Песочница, сохранение прогресса (SQLite), 10 уроков.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
import sys
import io
import sqlite3
from datetime import datetime


# ============ Стили ============
BTN_PINK = "#F8BBD0"
BTN_PINK_DARK = "#F06292"
BTN_GREEN = "#C8E6C9"
BTN_YELLOW = "#FFF9C4"

BTN_STYLE = Pack(margin=5, background_color=BTN_PINK)
BTN_MAIN_STYLE = Pack(margin=5, background_color=BTN_PINK_DARK)
BTN_ALT_STYLE = Pack(margin=5, background_color=BTN_GREEN)
BTN_SAND_STYLE = Pack(margin=5, background_color=BTN_YELLOW)


# ============ Данные уроков ============
LESSONS = [
    # ---------------- УРОК 1 ----------------
    {
        "title": "Урок 1: Переменные",
        "theory": (
            "ПЕРЕМЕННАЯ — это именованный контейнер для хранения данных. "
            "Когда вы пишете «x = 5», вы создаёте переменную x, которая "
            "хранит число 5.\n\n"

            "📌 ЗАЧЕМ НУЖНЫ ПЕРЕМЕННЫЕ\n"
            "Программа — это последовательность операций с данными. "
            "Чтобы данные где-то хранить и повторно использовать, "
            "придумали переменные. Вместо числа 25 пишете age — "
            "и Python подставляет значение.\n\n"

            "📌 КАК СОЗДАТЬ ПЕРЕМЕННУЮ\n"
            "name = 'Анна'\n"
            "Здесь name — имя, = — присваивание, 'Анна' — значение.\n\n"

            "📌 ПРАВИЛА ИМЕНОВАНИЯ\n"
            "• Буквы, цифры, знак _\n"
            "• Нельзя начинать с цифры\n"
            "• Регистр важен: name ≠ Name\n"
            "• Нельзя использовать служебные слова (print, for, if)\n\n"

            "📌 ТИПЫ ДАННЫХ\n"
            "• int — целые: 5, -10, 100\n"
            "• float — дробные: 3.14, 2.5\n"
            "• str — строки: 'Анна', 'Привет'\n"
            "• bool — True или False\n\n"

            "📌 ПРИМЕР 1. Числа и строки\n"
            "name = 'Анна'\n"
            "age = 25\n"
            "print(name)\n"
            "print(age)\n\n"

            "📌 ПРИМЕР 2. Операции\n"
            "x = 10\n"
            "y = 3\n"
            "print(x + y)  →  13\n"
            "print(x * y)  →  30\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Переменная создаётся при присваивании.\n"
            "2. Тип данных Python определяет сам.\n"
            "3. print() выводит значение на экран."
        ),
        "tasks": [
            {
                "task": "Создайте переменную со значением 7 и выведите её на экран.",
                "example": "number = 7\nprint(number)",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nnumber = 7\nprint(number)\n\n"
                    "Пошагово:\n"
                    "• number = 7 — создаём переменную\n"
                    "• print(number) — выводим её значение\n\n"
                    "Ожидаемый результат: 7"
                ),
                "expected_output": "7",
            },
            {
                "task": "Создайте переменные a = 6 и b = 4. Выведите их сумму и произведение.",
                "example": "a = 6\nb = 4\nprint(a + b)\nprint(a * b)",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\na = 6\nb = 4\nprint(a + b)\nprint(a * b)\n\n"
                    "Пошагово:\n"
                    "• a = 6, b = 4 — две переменные\n"
                    "• print(a + b) → 10\n"
                    "• print(a * b) → 24\n\n"
                    "Ожидаемый результат:\n10\n24"
                ),
                "expected_output": "10\n24",
            },
        ],
    },
    # ---------------- УРОК 2 ----------------
    {
        "title": "Урок 2: Цикл for",
        "theory": (
            "ЦИКЛ — конструкция, которая повторяет блок кода несколько раз. "
            "Цикл for используется, когда заранее известно количество "
            "повторений.\n\n"

            "📌 СИНТАКСИС\n"
            "for переменная in последовательность:\n"
            "    тело цикла\n\n"

            "📌 ФУНКЦИЯ range()\n"
            "• range(3)         → 0, 1, 2\n"
            "• range(1, 4)      → 1, 2, 3\n"
            "• range(0, 10, 2)  → 0, 2, 4, 6, 8\n\n"
            "ВАЖНО: правая граница НЕ входит в диапазон.\n\n"

            "📌 ПРИМЕР 1. Простой цикл\n"
            "for i in range(3):\n"
            "    print(i)\n"
            "Результат: 0, 1, 2 — каждое с новой строки.\n\n"

            "📌 ПРИМЕР 2. Цикл по строке\n"
            "word = 'Python'\n"
            "for letter in word:\n"
            "    print(letter)\n"
            "Результат: каждая буква на новой строке.\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Тело цикла выделяется ОТСТУПОМ в 4 пробела.\n"
            "2. Без отступа Python выдаст ошибку.\n"
            "3. Переменная цикла принимает значения по очереди."
        ),
        "tasks": [
            {
                "task": "Выведите числа от 0 до 4 с помощью цикла for.",
                "example": "for i in range(5):\n    print(i)",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nfor i in range(5):\n    print(i)\n\n"
                    "Пошагово:\n"
                    "• range(5) → 0, 1, 2, 3, 4\n"
                    "• i принимает каждое значение\n"
                    "• print(i) выводит текущее число\n\n"
                    "Ожидаемый результат:\n0\n1\n2\n3\n4"
                ),
                "expected_output": "0\n1\n2\n3\n4",
            },
            {
                "task": "Выведите буквы слова 'Кот' с помощью цикла for.",
                "example": "word = 'Кот'\nfor letter in word:\n    print(letter)",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nword = 'Кот'\nfor letter in word:\n    print(letter)\n\n"
                    "Пошагово:\n"
                    "• word — переменная со строкой\n"
                    "• Цикл проходит по каждой букве\n"
                    "• print выводит текущую букву\n\n"
                    "Ожидаемый результат:\nК\nо\nт"
                ),
                "expected_output": "К\nо\nт",
            },
        ],
    },
    # ---------------- УРОК 3 ----------------
    {
        "title": "Урок 3: Функции",
        "theory": (
            "ФУНКЦИЯ — блок кода, который можно вызывать многократно "
            "по имени.\n\n"

            "📌 СИНТАКСИС\n"
            "def имя_функции(параметры):\n"
            "    тело функции\n"
            "    return результат\n\n"

            "📌 КЛЮЧЕВОЕ СЛОВО return\n"
            "Возвращает значение из функции. Без return функция вернёт None.\n\n"

            "📌 ОБЪЯВЛЕНИЕ И ВЫЗОВ — РАЗНОЕ\n"
            "def square(x):\n"
            "    return x * x\n\n"
            "Объявление НЕ выполняет функцию. Нужно её вызвать:\n"
            "print(square(4))  →  16\n\n"

            "📌 ПРИМЕР 1. Функция с возвратом\n"
            "def square(x):\n"
            "    return x * x\n"
            "print(square(4))\n\n"

            "📌 ПРИМЕР 2. Два параметра\n"
            "def greet(name, age):\n"
            "    return f'Привет, {name}! Тебе {age} лет.'\n"
            "print(greet('Анна', 25))\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Функция сначала объявляется, потом вызывается.\n"
            "2. return завершает функцию и возвращает значение.\n"
            "3. Параметры — имена, аргументы — конкретные значения."
        ),
        "tasks": [
            {
                "task": "Напишите функцию square(x), возвращающую квадрат числа, и выведите square(6).",
                "example": "def square(x):\n    return x * x\nprint(square(6))",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\ndef square(x):\n    return x * x\nprint(square(6))\n\n"
                    "Пошагово:\n"
                    "• def square(x): — объявление\n"
                    "• return x * x — возврат квадрата\n"
                    "• square(6) → 36\n\n"
                    "Ожидаемый результат: 36"
                ),
                "expected_output": "36",
            },
            {
                "task": "Напишите функцию multiply(a, b), возвращающую произведение, и выведите multiply(3, 4).",
                "example": "def multiply(a, b):\n    return a * b\nprint(multiply(3, 4))",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\ndef multiply(a, b):\n    return a * b\nprint(multiply(3, 4))\n\n"
                    "Пошагово:\n"
                    "• Функция принимает a, b\n"
                    "• Возвращает произведение\n"
                    "• multiply(3, 4) → 12\n\n"
                    "Ожидаемый результат: 12"
                ),
                "expected_output": "12",
            },
        ],
    },
    # ---------------- УРОК 4 ----------------
    {
        "title": "Урок 4: Условия if",
        "theory": (
            "УСЛОВИЕ — конструкция, которая выполняет код только если "
            "выполняется проверка. Это позволяет программе «принимать "
            "решения».\n\n"

            "📌 СИНТАКСИС\n"
            "if условие:\n"
            "    код если True\n"
            "elif другое_условие:\n"
            "    код если первое False, второе True\n"
            "else:\n"
            "    код если всё False\n\n"

            "📌 ОПЕРАТОРЫ СРАВНЕНИЯ\n"
            "• ==  равно\n"
            "• !=  не равно\n"
            "• >   больше\n"
            "• <   меньше\n"
            "• >=  больше или равно\n"
            "• <=  меньше или равно\n\n"

            "📌 ЛОГИЧЕСКИЕ ОПЕРАТОРЫ\n"
            "• and — и то, и другое\n"
            "• or  — хотя бы одно\n"
            "• not — отрицание\n\n"

            "📌 ПРИМЕР 1. Проверка числа\n"
            "x = 10\n"
            "if x > 5:\n"
            "    print('больше 5')\n"
            "else:\n"
            "    print('не больше 5')\n\n"

            "📌 ПРИМЕР 2. С elif\n"
            "age = 18\n"
            "if age < 18:\n"
            "    print('ребёнок')\n"
            "elif age < 65:\n"
            "    print('взрослый')\n"
            "else:\n"
            "    print('пенсионер')\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Двоеточие после условия обязательно.\n"
            "2. Тело условия — с отступом 4 пробела.\n"
            "3. elif может быть много, else — только один."
        ),
        "tasks": [
            {
                "task": "Создайте переменную x = 15. Если x больше 10 — выведите 'big', иначе — 'small'.",
                "example": "x = 15\nif x > 10:\n    print('big')\nelse:\n    print('small')",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nx = 15\nif x > 10:\n    print('big')\nelse:\n    print('small')\n\n"
                    "Пошагово:\n"
                    "• x = 15\n"
                    "• 15 > 10 → True\n"
                    "• Выводится 'big'\n\n"
                    "Ожидаемый результат: big"
                ),
                "expected_output": "big",
            },
            {
                "task": "Дано число n = 7. Если оно чётное — выведите 'even', иначе — 'odd'.",
                "example": "n = 7\nif n % 2 == 0:\n    print('even')\nelse:\n    print('odd')",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nn = 7\nif n % 2 == 0:\n    print('even')\nelse:\n    print('odd')\n\n"
                    "Пошагово:\n"
                    "• % — остаток от деления\n"
                    "• 7 % 2 = 1, не ноль\n"
                    "• Условие False → else\n\n"
                    "Ожидаемый результат: odd"
                ),
                "expected_output": "odd",
            },
        ],
    },
    # ---------------- УРОК 5 ----------------
    {
        "title": "Урок 5: Списки",
        "theory": (
            "СПИСОК — упорядоченная коллекция элементов. Списки в Python "
            "заключаются в квадратные скобки.\n\n"

            "📌 СОЗДАНИЕ СПИСКА\n"
            "fruits = ['яблоко', 'банан', 'вишня']\n"
            "numbers = [1, 2, 3, 4, 5]\n"
            "mixed = [1, 'два', True, 3.14]\n\n"

            "📌 ДОСТУП ПО ИНДЕКСУ\n"
            "Индексация начинается с 0!\n"
            "fruits[0]  → 'яблоко'\n"
            "fruits[1]  → 'банан'\n"
            "fruits[-1] → 'вишня' (последний)\n\n"

            "📌 ОСНОВНЫЕ МЕТОДЫ\n"
            "• append(x) — добавить в конец\n"
            "• remove(x) — удалить элемент\n"
            "• len(list) — длина списка\n"
            "• sort() — отсортировать\n\n"

            "📌 ПРИМЕР 1. Создание и вывод\n"
            "colors = ['красный', 'зелёный', 'синий']\n"
            "print(colors[0])\n"
            "print(len(colors))\n"
            "Результат: красный, 3\n\n"

            "📌 ПРИМЕР 2. Перебор в цикле\n"
            "for fruit in ['яблоко', 'банан']:\n"
            "    print(fruit)\n"
            "Результат: яблоко, банан\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Индексы начинаются с 0.\n"
            "2. Отрицательный индекс идёт с конца.\n"
            "3. Список можно перебирать в цикле for."
        ),
        "tasks": [
            {
                "task": "Создайте список [10, 20, 30] и выведите первый элемент.",
                "example": "nums = [10, 20, 30]\nprint(nums[0])",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nnums = [10, 20, 30]\nprint(nums[0])\n\n"
                    "Пошагово:\n"
                    "• Создаём список из трёх чисел\n"
                    "• nums[0] — первый элемент\n\n"
                    "Ожидаемый результат: 10"
                ),
                "expected_output": "10",
            },
            {
                "task": "Создайте список ['a', 'b', 'c'] и выведите его длину (len).",
                "example": "letters = ['a', 'b', 'c']\nprint(len(letters))",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nletters = ['a', 'b', 'c']\nprint(len(letters))\n\n"
                    "Пошагово:\n"
                    "• Создаём список из 3 элементов\n"
                    "• len() возвращает количество\n\n"
                    "Ожидаемый результат: 3"
                ),
                "expected_output": "3",
            },
        ],
    },
    # ---------------- УРОК 6 ----------------
    {
        "title": "Урок 6: Цикл while",
        "theory": (
            "ЦИКЛ WHILE повторяется, пока условие истинно. В отличие от for, "
            "здесь не нужно заранее знать количество повторений.\n\n"

            "📌 СИНТАКСИС\n"
            "while условие:\n"
            "    тело цикла\n\n"

            "📌 КАК ЭТО РАБОТАЕТ\n"
            "Python проверяет условие:\n"
            "• True → выполняет тело, возвращается к проверке\n"
            "• False → выходит из цикла\n\n"

            "📌 ПРИМЕР 1. Счётчик\n"
            "i = 0\n"
            "while i < 3:\n"
            "    print(i)\n"
            "    i = i + 1\n"
            "Результат: 0, 1, 2\n\n"

            "📌 ПРИМЕР 2. Обратный отсчёт\n"
            "n = 3\n"
            "while n > 0:\n"
            "    print(n)\n"
            "    n = n - 1\n"
            "Результат: 3, 2, 1\n\n"

            "📌 БЕСКОНЕЧНЫЙ ЦИКЛ\n"
            "Если условие никогда не станет False — цикл будет вечным. "
            "Обязательно меняйте переменную внутри цикла!\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Условие проверяется ПЕРЕД каждой итерацией.\n"
            "2. Нужно менять переменную, иначе цикл не завершится.\n"
            "3. Используйте while, когда число повторений неизвестно."
        ),
        "tasks": [
            {
                "task": "С помощью while выведите числа от 1 до 3.",
                "example": "i = 1\nwhile i <= 3:\n    print(i)\n    i = i + 1",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\ni = 1\nwhile i <= 3:\n    print(i)\n    i = i + 1\n\n"
                    "Пошагово:\n"
                    "• i = 1, выводим 1, i = 2\n"
                    "• i = 2, выводим 2, i = 3\n"
                    "• i = 3, выводим 3, i = 4\n"
                    "• 4 <= 3 → False, выход\n\n"
                    "Ожидаемый результат:\n1\n2\n3"
                ),
                "expected_output": "1\n2\n3",
            },
            {
                "task": "С помощью while выведите числа от 5 до 1 в обратном порядке.",
                "example": "n = 5\nwhile n >= 1:\n    print(n)\n    n = n - 1",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nn = 5\nwhile n >= 1:\n    print(n)\n    n = n - 1\n\n"
                    "Пошагово:\n"
                    "• n уменьшается на 1 каждую итерацию\n"
                    "• Когда n станет 0, цикл завершится\n\n"
                    "Ожидаемый результат:\n5\n4\n3\n2\n1"
                ),
                "expected_output": "5\n4\n3\n2\n1",
            },
        ],
    },
    # ---------------- УРОК 7 ----------------
    {
        "title": "Урок 7: Словари",
        "theory": (
            "СЛОВАРЬ — коллекция пар «ключ: значение». В отличие от списка, "
            "доступ к элементам идёт по ключу, а не по индексу.\n\n"

            "📌 СОЗДАНИЕ\n"
            "person = {'name': 'Анна', 'age': 25}\n"
            "person = {'имя': 'Иван', 'возраст': 30}\n\n"

            "📌 ДОСТУП К ЗНАЧЕНИЮ\n"
            "person['name']   →  'Анна'\n"
            "person['age']    →  25\n\n"

            "📌 ДОБАВЛЕНИЕ И ИЗМЕНЕНИЕ\n"
            "person['city'] = 'Москва'   # добавить\n"
            "person['age'] = 26           # изменить\n\n"

            "📌 ПОЛЕЗНЫЕ МЕТОДЫ\n"
            "• keys()   — все ключи\n"
            "• values() — все значения\n"
            "• items()  — пары ключ-значение\n\n"

            "📌 ПРИМЕР 1. Доступ\n"
            "d = {'a': 1, 'b': 2}\n"
            "print(d['a'])\n"
            "Результат: 1\n\n"

            "📌 ПРИМЕР 2. Перебор\n"
            "for key in {'x': 1, 'y': 2}:\n"
            "    print(key)\n"
            "Результат: x, y\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Ключи уникальны — повторение перезапишет значение.\n"
            "2. Ключом может быть строка или число.\n"
            "3. Порядок в словаре не важен."
        ),
        "tasks": [
            {
                "task": "Создайте словарь {'a': 1} и выведите значение по ключу 'a'.",
                "example": "d = {'a': 1}\nprint(d['a'])",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nd = {'a': 1}\nprint(d['a'])\n\n"
                    "Ожидаемый результат: 1"
                ),
                "expected_output": "1",
            },
            {
                "task": "Создайте словарь {'x': 10, 'y': 20} и выведите сумму значений.",
                "example": "d = {'x': 10, 'y': 20}\nprint(d['x'] + d['y'])",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nd = {'x': 10, 'y': 20}\nprint(d['x'] + d['y'])\n\n"
                    "Пошагово:\n"
                    "• d['x'] = 10, d['y'] = 20\n"
                    "• 10 + 20 = 30\n\n"
                    "Ожидаемый результат: 30"
                ),
                "expected_output": "30",
            },
        ],
    },
    # ---------------- УРОК 8 ----------------
    {
        "title": "Урок 8: Строки",
        "theory": (
            "СТРОКА — последовательность символов в кавычках. У строк есть "
            "много встроенных методов.\n\n"

            "📌 СОЗДАНИЕ\n"
            "s1 = 'Привет'\n"
            "s2 = \"Мир\"\n"
            "s3 = 'Много\\nстрок'\n\n"

            "📌 ОСНОВНЫЕ ОПЕРАЦИИ\n"
            "• s.upper()   — в верхний регистр\n"
            "• s.lower()   — в нижний регистр\n"
            "• s.strip()   — убрать пробелы по краям\n"
            "• s.replace(a, b) — заменить\n"
            "• s.split(sep)    — разбить по разделителю\n"
            "• len(s)      — длина строки\n\n"

            "📌 ИНДЕКСЫ И СРЕЗЫ\n"
            "s = 'Python'\n"
            "s[0]     → 'P'\n"
            "s[-1]    → 'n'\n"
            "s[0:3]   → 'Pyt'\n\n"

            "📌 F-СТРОКИ\n"
            "name = 'Анна'\n"
            "age = 25\n"
            "print(f'{name} — {age} лет')\n"
            "Результат: Анна — 25 лет\n\n"

            "📌 ПРИМЕР 1. Методы\n"
            "s = '  Hello  '\n"
            "print(s.strip())\n"
            "print(s.upper())\n"
            "Результат: 'Hello', '  HELLO  '\n\n"

            "📌 ПРИМЕР 2. F-строка\n"
            "x = 5\n"
            "print(f'x = {x}')\n"
            "Результат: x = 5\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Строки неизменяемы — методы возвращают новую строку.\n"
            "2. Индексация с 0, срез [start:end] не включает end.\n"
            "3. F-строки — самый удобный способ подставить значения."
        ),
        "tasks": [
            {
                "task": "Дана строка s = 'hello'. Выведите её в верхнем регистре.",
                "example": "s = 'hello'\nprint(s.upper())",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\ns = 'hello'\nprint(s.upper())\n\n"
                    "Ожидаемый результат: HELLO"
                ),
                "expected_output": "HELLO",
            },
            {
                "task": "Дано имя name = 'Иван'. Выведите строку 'Привет, Иван!' через f-строку.",
                "example": "name = 'Иван'\nprint(f'Привет, {name}!')",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nname = 'Иван'\nprint(f'Привет, {name}!')\n\n"
                    "Пошагово:\n"
                    "• F-строка начинается с f перед кавычкой\n"
                    "• {name} подставит значение\n\n"
                    "Ожидаемый результат: Привет, Иван!"
                ),
                "expected_output": "Привет, Иван!",
            },
        ],
    },
    # ---------------- УРОК 9 ----------------
    {
        "title": "Урок 9: Исключения",
        "theory": (
            "ИСКЛЮЧЕНИЕ — это ошибка, которая возникает во время работы "
            "программы. Их можно перехватывать и обрабатывать.\n\n"

            "📌 ЗАЧЕМ\n"
            "Программа не должна падать при ошибке. Например, если "
            "пользователь ввёл текст вместо числа — нужно вежливо "
            "сообщить, а не вылетать.\n\n"

            "📌 СИНТАКСИС\n"
            "try:\n"
            "    код_который_может_упасть\n"
            "except ТипОшибки:\n"
            "    что_делать_при_ошибке\n"
            "else:\n"
            "    если_ошибки_не_было\n"
            "finally:\n"
            "    выполнится_в_любом_случае\n\n"

            "📌 ТИПЫ ОШИБОК\n"
            "• ZeroDivisionError — деление на ноль\n"
            "• ValueError — неверное значение\n"
            "• TypeError — неверный тип\n"
            "• KeyError — нет ключа в словаре\n"
            "• IndexError — индекс вне списка\n\n"

            "📌 ПРИМЕР 1. Деление\n"
            "try:\n"
            "    print(10 / 0)\n"
            "except ZeroDivisionError:\n"
            "    print('Деление на ноль!')\n\n"

            "📌 ПРИМЕР 2. Сообщение об ошибке\n"
            "try:\n"
            "    x = int('abc')\n"
            "except ValueError as e:\n"
            "    print(f'Ошибка: {e}')\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. try-блок — опасный код, except — обработка.\n"
            "2. Ошибки не падают насовсем — их можно поймать.\n"
            "3. Лучше указывать конкретный тип ошибки."
        ),
        "tasks": [
            {
                "task": "С помощью try/except обработайте деление 10 / 0 и выведите 'error'.",
                "example": "try:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print('error')",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\ntry:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print('error')\n\n"
                    "Ожидаемый результат: error"
                ),
                "expected_output": "error",
            },
            {
                "task": "Обработайте ошибку int('abc') через try/except и выведите 'fail'.",
                "example": "try:\n    x = int('abc')\nexcept ValueError:\n    print('fail')",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\ntry:\n    x = int('abc')\nexcept ValueError:\n    print('fail')\n\n"
                    "Пошагово:\n"
                    "• int('abc') вызовет ValueError\n"
                    "• except поймает и выведет 'fail'\n\n"
                    "Ожидаемый результат: fail"
                ),
                "expected_output": "fail",
            },
        ],
    },
    # ---------------- УРОК 10 ----------------
    {
        "title": "Урок 10: Модули и импорт",
        "theory": (
            "МОДУЛЬ — это файл с кодом, который можно подключить к своей "
            "программе. В Python сотни встроенных модулей.\n\n"

            "📌 СИНТАКСИС ИМПОРТА\n"
            "import math                 # весь модуль\n"
            "from math import sqrt       # конкретная функция\n"
            "import math as m            # переименовать\n\n"

            "📌 ПОЛЕЗНЫЕ МОДУЛИ\n"
            "• math — математика (sqrt, pi, sin)\n"
            "• random — случайные числа\n"
            "• datetime — дата и время\n"
            "• os — работа с файлами\n\n"

            "📌 ПРИМЕР 1. math\n"
            "import math\n"
            "print(math.sqrt(16))\n"
            "Результат: 4.0\n\n"

            "📌 ПРИМЕР 2. random\n"
            "import random\n"
            "n = random.randint(1, 10)\n"
            "print(n)\n"
            "Результат: случайное число от 1 до 10\n\n"

            "📌 ПРИМЕР 3. Из модуля напрямую\n"
            "from math import pi\n"
            "print(pi)\n"
            "Результат: 3.141592653589793\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. import ставится в начале файла.\n"
            "2. Можно импортировать функции по одной.\n"
            "3. Свой модуль — это просто .py файл."
        ),
        "tasks": [
            {
                "task": "Импортируйте math и выведите math.sqrt(25).",
                "example": "import math\nprint(math.sqrt(25))",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nimport math\nprint(math.sqrt(25))\n\n"
                    "Пошагово:\n"
                    "• Импортируем модуль math\n"
                    "• math.sqrt(25) → 5.0\n\n"
                    "Ожидаемый результат: 5.0"
                ),
                "expected_output": "5.0",
            },
            {
                "task": "Импортируйте pi из math и выведите round(pi, 2).",
                "example": "from math import pi\nprint(round(pi, 2))",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Код решения:\nfrom math import pi\nprint(round(pi, 2))\n\n"
                    "Пошагово:\n"
                    "• from math import pi — берём только pi\n"
                    "• round(pi, 2) — округляем до 2 знаков\n\n"
                    "Ожидаемый результат: 3.14"
                ),
                "expected_output": "3.14",
            },
        ],
    },
]


# ============ Главный класс приложения ============
class LearnPythonApp(toga.App):

    def startup(self):
        self.current_lesson_index = 0
        self.current_task_index = 0

        self._init_db()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.build_lesson_list_screen()
        self.main_window.show()

    # ---------- База данных ----------
    def _db_path(self):
        return str(self.paths.data / "progress.db")

    def _init_db(self):
        self.db = sqlite3.connect(self._db_path())
        cur = self.db.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS completed (
                lesson_idx INTEGER,
                task_idx INTEGER,
                completed_at TEXT,
                PRIMARY KEY (lesson_idx, task_idx)
            )
        """)
        self.db.commit()

    def mark_completed(self, lesson_idx, task_idx):
        cur = self.db.cursor()
        cur.execute(
            "INSERT OR REPLACE INTO completed VALUES (?, ?, ?)",
            (lesson_idx, task_idx, datetime.now().isoformat()),
        )
        self.db.commit()

    def is_completed(self, lesson_idx, task_idx):
        cur = self.db.cursor()
        cur.execute(
            "SELECT 1 FROM completed WHERE lesson_idx=? AND task_idx=?",
            (lesson_idx, task_idx),
        )
        return cur.fetchone() is not None

    def count_completed(self, lesson_idx):
        cur = self.db.cursor()
        cur.execute(
            "SELECT COUNT(*) FROM completed WHERE lesson_idx=?",
            (lesson_idx,),
        )
        return cur.fetchone()[0]

    # ---------- Экран 1: список уроков ----------
    def build_lesson_list_screen(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=15, flex=1))

        title_label = toga.Label(
            "🐍 Уроки Python",
            style=Pack(font_size=24, font_weight="bold",
                       margin_bottom=10, text_align=CENTER),
        )
        main_box.add(title_label)

        total_tasks = sum(len(l["tasks"]) for l in LESSONS)
        done_tasks = sum(self.count_completed(i) for i in range(len(LESSONS)))
        progress = toga.Label(
            f"Прогресс: {done_tasks} / {total_tasks} задач",
            style=Pack(font_size=13, margin_bottom=10, text_align=CENTER),
        )
        main_box.add(progress)

        lessons_box = toga.Box(style=Pack(direction=COLUMN, margin=5))
        scroll = toga.ScrollContainer(
            content=lessons_box, style=Pack(flex=1), horizontal=False,
        )

        for index, lesson in enumerate(LESSONS):
            done = self.count_completed(index)
            total = len(lesson["tasks"])
            if done == total:
                mark = "✅"
            elif done > 0:
                mark = f"▶ {done}/{total}"
            else:
                mark = "•"

            btn = toga.Button(
                f"{mark}  {index + 1}. {lesson['title']}",
                on_press=self.open_lesson,
                style=BTN_STYLE,
            )
            btn.lesson_index = index
            lessons_box.add(btn)

        main_box.add(scroll)

        sandbox_btn = toga.Button(
            "🧪 Песочница (свободный код)",
            on_press=self.open_sandbox,
            style=BTN_SAND_STYLE,
        )
        main_box.add(sandbox_btn)

        reset_btn = toga.Button(
            "🗑 Сбросить прогресс",
            on_press=self.reset_progress,
            style=BTN_STYLE,
        )
        main_box.add(reset_btn)

        return main_box

    def reset_progress(self, widget):
        cur = self.db.cursor()
        cur.execute("DELETE FROM completed")
        self.db.commit()
        self.main_window.content = self.build_lesson_list_screen()

    # ---------- Экран 2: теория ----------
    def open_lesson(self, widget):
        self.current_lesson_index = widget.lesson_index
        lesson = LESSONS[self.current_lesson_index]

        main_box = toga.Box(style=Pack(direction=COLUMN, margin=10, flex=1))

        back_btn = toga.Button(
            "← Назад к списку",
            on_press=self.go_back_to_list,
            style=BTN_STYLE,
        )
        main_box.add(back_btn)

        self.theory_view = toga.MultilineTextInput(
            readonly=True,
            value=lesson["theory"],
            style=Pack(flex=1, margin=5),
        )
        main_box.add(self.theory_view)

        practice_btn = toga.Button(
            "💻 Перейти к практике",
            on_press=self.open_practice_screen,
            style=BTN_MAIN_STYLE,
        )
        main_box.add(practice_btn)

        self.main_window.content = main_box

    def go_back_to_list(self, widget):
        self.main_window.content = self.build_lesson_list_screen()

    # ---------- Экран 3: практика ----------
    def open_practice_screen(self, widget):
        self.current_task_index = 0
        self.render_practice_screen()

    def render_practice_screen(self):
        lesson = LESSONS[self.current_lesson_index]
        task = lesson["tasks"][self.current_task_index]

        main_box = toga.Box(style=Pack(direction=COLUMN, margin=10, flex=1))

        back_btn = toga.Button(
            "← Назад к теории",
            on_press=self.go_back_to_theory,
            style=BTN_STYLE,
        )
        main_box.add(back_btn)

        if len(lesson["tasks"]) > 1:
            switch_row = toga.Box(style=Pack(direction=ROW, margin=5))
            for idx, t in enumerate(lesson["tasks"]):
                label = f"Задача {idx + 1}"
                if self.is_completed(self.current_lesson_index, idx):
                    label = f"✅ {label}"
                if idx == self.current_task_index:
                    label = f"▶ {label}"
                btn = toga.Button(
                    label,
                    on_press=self.switch_task,
                    style=Pack(flex=1, margin_left=2, margin_right=2,
                               background_color=BTN_PINK),
                )
                btn.task_index = idx
                switch_row.add(btn)
            main_box.add(switch_row)

        task_header = toga.Label(
            "📝 Условие задачи:",
            style=Pack(font_size=13, font_weight="bold",
                       margin_left=5, margin_top=5),
        )
        main_box.add(task_header)

        task_text = toga.MultilineTextInput(
            readonly=True,
            value=task["task"],
            style=Pack(flex=1, margin=5),
        )
        main_box.add(task_text)

        example_label = toga.Label(
            "Пример:",
            style=Pack(font_size=13, font_weight="bold",
                       margin_left=5, margin_top=5),
        )
        main_box.add(example_label)

        example_code = toga.MultilineTextInput(
            readonly=True,
            value=task.get("example", ""),
            style=Pack(flex=2, margin=5),
        )
        main_box.add(example_code)

        self.code_editor = toga.MultilineTextInput(
            placeholder="Введите ваш код здесь...",
            style=Pack(flex=3, margin=5),
        )
        main_box.add(self.code_editor)

        btn_row = toga.Box(style=Pack(direction=ROW, margin=5))
        run_btn = toga.Button(
            "▶ Запустить",
            on_press=self.run_code,
            style=Pack(flex=1, margin_right=5, background_color=BTN_PINK),
        )
        check_btn = toga.Button(
            "✅ Проверить",
            on_press=self.check_answer,
            style=Pack(flex=1, margin_left=5, background_color=BTN_PINK),
        )
        btn_row.add(run_btn)
        btn_row.add(check_btn)
        main_box.add(btn_row)

        explain_btn = toga.Button(
            "💡 Показать разбор",
            on_press=self.show_explanation,
            style=BTN_MAIN_STYLE,
        )
        main_box.add(explain_btn)

        self.output_text = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=2, margin=5),
        )
        main_box.add(self.output_text)

        self.main_window.content = main_box

    def switch_task(self, widget):
        self.current_task_index = widget.task_index
        self.render_practice_screen()

    def go_back_to_theory(self, widget):
        class FakeWidget:
            pass
        w = FakeWidget()
        w.lesson_index = self.current_lesson_index
        self.open_lesson(w)

    # ---------- Песочница ----------
    def open_sandbox(self, widget):
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=10, flex=1))

        back_btn = toga.Button(
            "← Назад к списку",
            on_press=self.go_back_to_list,
            style=BTN_STYLE,
        )
        main_box.add(back_btn)

        title = toga.Label(
            "🧪 Песочница — пишите любой код",
            style=Pack(font_size=16, font_weight="bold",
                       margin=5, text_align=CENTER),
        )
        main_box.add(title)

        self.sandbox_editor = toga.MultilineTextInput(
            placeholder="Введите любой код на Python...\nНапример: print('Привет!')",
            style=Pack(flex=2, margin=5),
        )
        main_box.add(self.sandbox_editor)

        run_btn = toga.Button(
            "▶ Запустить код",
            on_press=self.run_sandbox,
            style=BTN_MAIN_STYLE,
        )
        main_box.add(run_btn)

        clear_btn = toga.Button(
            "🗑 Очистить",
            on_press=self.clear_sandbox,
            style=BTN_STYLE,
        )
        main_box.add(clear_btn)

        self.sandbox_output = toga.MultilineTextInput(
            readonly=True,
            placeholder="Результат появится здесь...",
            style=Pack(flex=2, margin=5),
        )
        main_box.add(self.sandbox_output)

        self.main_window.content = main_box

    def run_sandbox(self, widget):
        code = self.sandbox_editor.value
        result = self.execute_code(code)
        self.sandbox_output.value = result if result else "(Нет вывода)"

    def clear_sandbox(self, widget):
        self.sandbox_editor.value = ""
        self.sandbox_output.value = ""

    # ---------- Логика ----------
    def execute_code(self, code):
        old_stdout = sys.stdout
        redirected = io.StringIO()
        sys.stdout = redirected
        try:
            exec(code, {})
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            sys.stdout = old_stdout
        return redirected.getvalue().strip()

    def run_code(self, widget):
        code = self.code_editor.value
        result = self.execute_code(code)
        self.output_text.value = result if result else "(Нет вывода)"

    def show_explanation(self, widget):
        lesson = LESSONS[self.current_lesson_index]
        task = lesson["tasks"][self.current_task_index]
        self.output_text.value = task["explanation"]

    def check_answer(self, widget):
        code = self.code_editor.value
        user_output = self.execute_code(code)
        lesson = LESSONS[self.current_lesson_index]
        expected = lesson["tasks"][self.current_task_index]["expected_output"].strip()

        if user_output == expected:
            self.mark_completed(self.current_lesson_index, self.current_task_index)
            self.output_text.value = "✅ Верно! Отличная работа.\n\nПрогресс сохранён."
        else:
            self.output_text.value = (
                f"❌ Не совсем.\n\n"
                f"Ожидалось:\n{expected}\n\n"
                f"Ваш вывод:\n{user_output if user_output else '(пусто)'}"
            )


def main():
    return LearnPythonApp()
