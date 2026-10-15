"""
Приложение для изучения Python — версия 2.4
- Кнопки задач: активная — розовая, неактивная — фиолетовая (без скобок)
- Пример: увеличен
- Результат: уменьшен
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
import sys
import io
import sqlite3
from datetime import datetime
from contextlib import redirect_stdout


# ============ Стили ============
BTN_PRIMARY = "#C2185B"
BTN_SECONDARY = "#7B1FA2"
BTN_SUCCESS = "#2E7D32"
BTN_ACCENT = "#F9A825"

BTN_STYLE = Pack(margin=5, background_color=BTN_SECONDARY)
BTN_MAIN_STYLE = Pack(margin=5, background_color=BTN_PRIMARY)
BTN_ACCENT_STYLE = Pack(margin=5, background_color=BTN_ACCENT)


# ============ Ачивки ============
ACHIEVEMENTS = {
    "first_step": "Первая переменная — пройдена первая задача!",
    "half_way": "Половина пути — пройдено 50% курса!",
    "cycle_master": "Мастер циклов — все задачи с циклами!",
    "function_guru": "Гуру функций — все задачи по функциям!",
    "all_done": "Курс пройден — все уроки завершены!",
}


# ============ Данные уроков ============
LESSONS = [
    {
        "title": "Переменные",
        "theory": (
            "ПЕРЕМЕННАЯ — это именованный контейнер для хранения данных. "
            "Когда вы пишете «x = 5», вы создаёте переменную x, которая "
            "хранит число 5. Переменная — это как коробка с наклейкой: "
            "на наклейке написано имя, а внутри лежит значение.\n\n"

            "ЗАЧЕМ НУЖНЫ ПЕРЕМЕННЫЕ\n"
            "Программа — это последовательность операций с данными. "
            "Чтобы эти данные где-то хранить и повторно использовать, "
            "придумали переменные. Вместо того чтобы каждый раз писать "
            "число 25, вы пишете age — и Python подставляет значение.\n\n"

            "КАК СОЗДАТЬ ПЕРЕМЕННУЮ\n"
            "В Python переменная создаётся в момент присваивания:\n"
            "name = 'Анна'\n"
            "Здесь name — имя переменной, = — оператор присваивания, "
            "'Анна' — значение. После этой строки Python запоминает: "
            "«переменная name содержит строку Анна».\n\n"

            "ПРАВИЛА ИМЕНОВАНИЯ\n"
            "• Имя может содержать латинские и русские буквы, цифры и знак _\n"
            "• Имя НЕ может начинаться с цифры: 5x — ошибка, x5 — ок\n"
            "• Нельзя использовать пробелы и знаки препинания\n"
            "• Регистр важен: name и Name — это РАЗНЫЕ переменные\n"
            "• Нельзя называть переменную служебным словом\n"
            "  (print, for, if, while и т.д.)\n"
            "• Имя должно быть осмысленным: age лучше, чем a\n\n"

            "ТИПЫ ДАННЫХ\n"
            "Python — язык с динамической типизацией. Это значит, что "
            "вам НЕ нужно указывать тип переменной — Python сам "
            "определяет его по значению.\n\n"
            "Основные типы:\n"
            "• int — целые числа: 5, -10, 100, 2024\n"
            "• float — дробные числа: 3.14, 2.5, -0.7\n"
            "• str — строки в кавычках: 'Анна', 'Привет'\n"
            "• bool — логические значения: True или False\n\n"

            "ПРИМЕР 1. Числа и строки\n"
            "name = 'Анна'\n"
            "age = 25\n"
            "print(name)\n"
            "print(age)\n"
            "Результат:\n"
            "Анна\n"
            "25\n\n"

            "ПРИМЕР 2. Операции с переменными\n"
            "x = 10\n"
            "y = 3\n"
            "print(x + y)   →  13\n"
            "print(x * y)   →  30\n"
            "print(x - y)   →  7\n"
            "print(x / y)   →  3.333...\n\n"

            "ФУНКЦИЯ print()\n"
            "print() — это встроенная функция вывода на экран. "
            "Внутри скобок пишется то, что нужно вывести. "
            "Можно выводить значения переменных, числа, строки, "
            "а также их комбинации через запятую:\n"
            "print('Возраст:', age)\n"
            "Результат: Возраст: 25\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. Переменная создаётся в момент присваивания через =.\n"
            "2. Тип данных Python определяет автоматически.\n"
            "3. Одно и то же имя можно перезаписать новым значением.\n"
            "4. print() нужен для того, чтобы увидеть результат."
        ),
        "tasks": [
            {
                "task": "Создайте переменную со значением 7 и выведите её на экран.",
                "example_task": "Создайте переменную со значением 3 и выведите её на экран.",
                "example": "number = 3\nprint(number)",
                "hint": "Сначала присвойте значение, потом используйте print().",
                "explanation": (
                    "Код решения:\nnumber = 7\nprint(number)\n\n"
                    "Ожидаемый результат: 7"
                ),
                "expected_output": "7",
            },
            {
                "task": "Создайте переменные a = 6 и b = 4. Выведите их сумму и произведение.",
                "example_task": "Создайте переменные a = 2 и b = 5. Выведите их сумму и произведение.",
                "example": "a = 2\nb = 5\nprint(a + b)\nprint(a * b)",
                "hint": "Сумма — это +, произведение — это *. Каждое с новой строки.",
                "explanation": (
                    "Код решения:\na = 6\nb = 4\nprint(a + b)\nprint(a * b)\n\n"
                    "Ожидаемый результат:\n10\n24"
                ),
                "expected_output": "10\n24",
            },
        ],
    },
    {
        "title": "Цикл for",
        "theory": (
            "ЦИКЛ — это конструкция, которая повторяет блок кода несколько "
            "раз. Цикл for используется, когда заранее известно количество "
            "повторений.\n\n"

            "ЗАЧЕМ НУЖНЫ ЦИКЛЫ\n"
            "Представьте, что нужно вывести на экран числа от 1 до 100. "
            "Можно написать 100 строк print() — а можно 2 строки с циклом. "
            "Циклы делают программы в десятки раз короче и понятнее. "
            "Это одна из главных идей программирования.\n\n"

            "СИНТАКСИС ЦИКЛА for\n"
            "for переменная in последовательность:\n"
            "    тело цикла\n\n"
            "Разбор:\n"
            "• for — ключевое слово, начало цикла\n"
            "• переменная — имя, которое принимает значения\n"
            "• in — ключевое слово\n"
            "• последовательность — откуда берутся значения\n"
            "• двоеточие в конце строки обязательно\n"
            "• тело цикла — с отступом в 4 пробела\n\n"

            "КАК РАБОТАЕТ ЦИКЛ\n"
            "Python по очереди берёт значения из последовательности, "
            "кладёт в переменную и выполняет тело цикла. Когда значения "
            "заканчиваются — цикл завершается.\n\n"

            "ФУНКЦИЯ range()\n"
            "range() создаёт последовательность чисел. У неё три формы:\n\n"
            "1. range(N) — от 0 до N-1:\n"
            "   range(3)      → 0, 1, 2\n"
            "   range(5)      → 0, 1, 2, 3, 4\n\n"
            "2. range(A, B) — от A до B-1:\n"
            "   range(1, 4)   → 1, 2, 3\n"
            "   range(2, 6)   → 2, 3, 4, 5\n\n"
            "3. range(A, B, step) — с шагом:\n"
            "   range(0, 10, 2)  → 0, 2, 4, 6, 8\n"
            "   range(10, 0, -2) → 10, 8, 6, 4, 2\n\n"
            "ВАЖНО: правая граница НЕ входит в диапазон!\n"
            "range(3) даёт 0, 1, 2 — но не 3.\n\n"

            "ПРИМЕР 1. Простой цикл\n"
            "for i in range(3):\n"
            "    print(i)\n\n"
            "Пошагово:\n"
            "1. range(3) создаёт значения 0, 1, 2\n"
            "2. i = 0 → print выводит 0\n"
            "3. i = 1 → print выводит 1\n"
            "4. i = 2 → print выводит 2\n"
            "5. Значения закончились, цикл завершён\n\n"

            "ПРИМЕР 2. Цикл по строке\n"
            "word = 'Python'\n"
            "for letter in word:\n"
            "    print(letter)\n\n"
            "Python выводит по одной букве: P, y, t, h, o, n. "
            "Строка — это тоже последовательность символов.\n\n"

            "ПРИМЕР 3. Обратный отсчёт\n"
            "for i in range(5, 0, -1):\n"
            "    print(i)\n"
            "Результат: 5, 4, 3, 2, 1\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. Тело цикла выделяется ОТСТУПОМ в 4 пробела.\n"
            "2. Без отступа Python выдаст ошибку.\n"
            "3. Имя переменной цикла может быть любым (i, j, x).\n"
            "4. Все действия с отступом выполняются на каждой итерации."
        ),
        "tasks": [
            {
                "task": "Выведите числа от 0 до 4 с помощью цикла for.",
                "example_task": "Выведите числа от 0 до 2 с помощью цикла for.",
                "example": "for i in range(3):\n    print(i)",
                "hint": "range(N) даёт N чисел начиная с 0. Для 0..4 нужно range(5).",
                "explanation": (
                    "Код решения:\nfor i in range(5):\n    print(i)\n\n"
                    "Ожидаемый результат:\n0\n1\n2\n3\n4"
                ),
                "expected_output": "0\n1\n2\n3\n4",
            },
            {
                "task": "Выведите буквы слова 'Кот' с помощью цикла for.",
                "example_task": "Выведите буквы слова 'Дом' с помощью цикла for.",
                "example": "word = 'Дом'\nfor letter in word:\n    print(letter)",
                "hint": "Цикл по строке перебирает буквы по одной.",
                "explanation": (
                    "Код решения:\nword = 'Кот'\nfor letter in word:\n    print(letter)\n\n"
                    "Ожидаемый результат:\nК\nо\nт"
                ),
                "expected_output": "К\nо\nт",
            },
        ],
    },
    {
        "title": "Функции",
        "theory": (
            "ФУНКЦИЯ — это блок кода, который можно вызывать многократно "
            "по имени. Функции делают программу короче, понятнее и "
            "удобнее для повторного использования.\n\n"

            "ЗАЧЕМ НУЖНЫ ФУНКЦИИ\n"
            "Представьте, что в программе нужно 10 раз посчитать площадь "
            "прямоугольника. Можно 10 раз написать формулу — а можно "
            "один раз создать функцию и вызывать её. Если формула "
            "изменится — править придётся в одном месте.\n\n"

            "СИНТАКСИС ОБЪЯВЛЕНИЯ\n"
            "def имя_функции(параметры):\n"
            "    тело функции\n"
            "    return результат\n\n"
            "Разбор:\n"
            "• def — ключевое слово (от английского define)\n"
            "• имя_функции — придумываете сами\n"
            "• параметры — данные, которые функция принимает\n"
            "• двоеточие в конце строки обязательно\n"
            "• тело функции — с отступом в 4 пробела\n"
            "• return — возвращает результат наружу\n\n"

            "КЛЮЧЕВОЕ СЛОВО return\n"
            "return выполняет две роли:\n"
            "1. Возвращает значение туда, откуда вызвали функцию\n"
            "2. Завершает выполнение функции\n\n"
            "Если не написать return — функция вернёт None.\n\n"

            "ОБЪЯВЛЕНИЕ И ВЫЗОВ — ЭТО РАЗНОЕ\n"
            "Объявление функции — это её описание:\n"
            "def square(x):\n"
            "    return x * x\n\n"
            "После объявления функция НИЧЕГО не делает. Чтобы она "
            "сработала, её нужно ВЫЗВАТЬ:\n"
            "print(square(4))   →  16\n\n"
            "Вызов — это имя функции со скобками и аргументами.\n\n"

            "ПРИМЕР 1. Функция с возвратом\n"
            "def square(x):\n"
            "    return x * x\n"
            "print(square(4))\n\n"
            "Пошагово:\n"
            "1. square(4) — вызываем функцию, x = 4\n"
            "2. Внутри: return 4 * 4 → 16\n"
            "3. Функция возвращает 16\n"
            "4. print выводит 16\n\n"

            "ПРИМЕР 2. Функция с двумя параметрами\n"
            "def greet(name, age):\n"
            "    return f'Привет, {name}! Тебе {age} лет.'\n"
            "print(greet('Анна', 25))\n\n"
            "Функция принимает два параметра и возвращает строку. "
            "F-строка (f'...') — это удобный способ вставить "
            "значение переменной прямо в текст.\n\n"

            "ПАРАМЕТРЫ И АРГУМЕНТЫ\n"
            "Параметры — это имена внутри объявления функции.\n"
            "Аргументы — это конкретные значения при вызове.\n"
            "def add(a, b):    ← a и b это параметры\n"
            "add(3, 5)         ← 3 и 5 это аргументы\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. Функция сначала ОБЪЯВЛЯЕТСЯ (def), а потом ВЫЗЫВАЕТСЯ.\n"
            "2. return завершает функцию и возвращает значение.\n"
            "3. Имя функции должно быть осмысленным.\n"
            "4. Внутри функции можно использовать любые конструкции."
        ),
        "tasks": [
            {
                "task": "Напишите функцию square(x), возвращающую квадрат, и выведите square(6).",
                "example_task": "Напишите функцию square(x), возвращающую квадрат, и выведите square(4).",
                "example": "def square(x):\n    return x * x\nprint(square(4))",
                "hint": "Квадрат — это x * x. Не забудьте return.",
                "explanation": (
                    "Код решения:\ndef square(x):\n    return x * x\nprint(square(6))\n\n"
                    "Ожидаемый результат: 36"
                ),
                "expected_output": "36",
            },
            {
                "task": "Напишите функцию multiply(a, b), возвращающую произведение, и выведите multiply(3, 4).",
                "example_task": "Напишите функцию multiply(a, b), возвращающую произведение, и выведите multiply(2, 5).",
                "example": "def multiply(a, b):\n    return a * b\nprint(multiply(2, 5))",
                "hint": "Произведение — это a * b.",
                "explanation": (
                    "Код решения:\ndef multiply(a, b):\n    return a * b\nprint(multiply(3, 4))\n\n"
                    "Ожидаемый результат: 12"
                ),
                "expected_output": "12",
            },
        ],
    },
    {
        "title": "Условия if",
        "theory": (
            "УСЛОВИЕ — конструкция, которая выполняет код только если "
            "выполняется проверка. Это позволяет программе «принимать "
            "решения».\n\n"

            "ЗАЧЕМ НУЖНЫ УСЛОВИЯ\n"
            "Программа должна уметь реагировать на разные ситуации. "
            "Например: если возраст меньше 18 — вывести «ребёнок», "
            "иначе — «взрослый». Это делается через if.\n\n"

            "СИНТАКСИС\n"
            "if условие:\n"
            "    код_если_true\n"
            "elif другое_условие:\n"
            "    код_если_первое_false_второе_true\n"
            "else:\n"
            "    код_если_всё_false\n\n"
            "Разбор:\n"
            "• if — начало условия\n"
            "• elif — «иначе если» (может быть много)\n"
            "• else — «иначе» (только один, идёт в конце)\n"
            "• тело каждого блока — с отступом 4 пробела\n\n"

            "ОПЕРАТОРЫ СРАВНЕНИЯ\n"
            "• ==  равно\n"
            "• !=  не равно\n"
            "• >   больше\n"
            "• <   меньше\n"
            "• >=  больше или равно\n"
            "• <=  меньше или равно\n\n"
            "ВАЖНО: = это присваивание, == это сравнение!\n\n"

            "ЛОГИЧЕСКИЕ ОПЕРАТОРЫ\n"
            "• and — и то, и другое\n"
            "• or  — хотя бы одно\n"
            "• not — отрицание\n\n"

            "ПРИМЕР 1. Проверка числа\n"
            "x = 10\n"
            "if x > 5:\n"
            "    print('больше 5')\n"
            "else:\n"
            "    print('не больше 5')\n"
            "Результат: больше 5\n\n"

            "ПРИМЕР 2. С elif\n"
            "age = 18\n"
            "if age < 18:\n"
            "    print('ребёнок')\n"
            "elif age < 65:\n"
            "    print('взрослый')\n"
            "else:\n"
            "    print('пенсионер')\n"
            "Результат: взрослый\n\n"

            "ПРИМЕР 3. Остаток от деления\n"
            "n = 7\n"
            "if n % 2 == 0:\n"
            "    print('чётное')\n"
            "else:\n"
            "    print('нечётное')\n"
            "Результат: нечётное\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. Двоеточие после условия обязательно.\n"
            "2. Тело условия — с отступом 4 пробела.\n"
            "3. elif может быть много, else — только один.\n"
            "4. Условия можно комбинировать через and / or / not."
        ),
        "tasks": [
            {
                "task": "Создайте x = 15. Если x больше 10 — выведите 'big', иначе 'small'.",
                "example_task": "Создайте x = 5. Если x больше 10 — выведите 'big', иначе 'small'.",
                "example": "x = 5\nif x > 10:\n    print('big')\nelse:\n    print('small')",
                "hint": "Используйте if/else. Проверка: x > 10.",
                "explanation": (
                    "Код решения:\nx = 15\nif x > 10:\n    print('big')\nelse:\n    print('small')\n\n"
                    "Ожидаемый результат: big"
                ),
                "expected_output": "big",
            },
            {
                "task": "Дано n = 7. Если n чётное — выведите 'even', иначе 'odd'.",
                "example_task": "Дано n = 4. Если n чётное — выведите 'even', иначе 'odd'.",
                "example": "n = 4\nif n % 2 == 0:\n    print('even')\nelse:\n    print('odd')",
                "hint": "Чётное число делится на 2 без остатка: n % 2 == 0.",
                "explanation": (
                    "Код решения:\nn = 7\nif n % 2 == 0:\n    print('even')\nelse:\n    print('odd')\n\n"
                    "Ожидаемый результат: odd"
                ),
                "expected_output": "odd",
            },
        ],
    },
    {
        "title": "Списки",
        "theory": (
            "СПИСОК — упорядоченная коллекция элементов. Списки в Python "
            "заключаются в квадратные скобки.\n\n"

            "ЗАЧЕМ НУЖНЫ СПИСКИ\n"
            "Вместо того чтобы хранить 100 чисел в 100 переменных, "
            "можно хранить их в одном списке и обращаться по индексу.\n\n"

            "СОЗДАНИЕ СПИСКА\n"
            "fruits = ['яблоко', 'банан', 'вишня']\n"
            "numbers = [1, 2, 3, 4, 5]\n"
            "mixed = [1, 'два', True, 3.14]\n\n"

            "ДОСТУП ПО ИНДЕКСУ\n"
            "Индексация начинается с 0!\n"
            "fruits[0]  → 'яблоко'\n"
            "fruits[1]  → 'банан'\n"
            "fruits[-1] → 'вишня' (последний)\n\n"

            "ОСНОВНЫЕ МЕТОДЫ\n"
            "• append(x) — добавить в конец\n"
            "• remove(x) — удалить элемент\n"
            "• len(list) — длина списка\n"
            "• sort() — отсортировать\n\n"

            "ПРИМЕР 1. Создание и вывод\n"
            "colors = ['красный', 'зелёный', 'синий']\n"
            "print(colors[0])\n"
            "print(len(colors))\n"
            "Результат: красный, 3\n\n"

            "ПРИМЕР 2. Перебор в цикле\n"
            "for fruit in ['яблоко', 'банан']:\n"
            "    print(fruit)\n"
            "Результат: яблоко, банан\n\n"

            "ПРИМЕР 3. Добавление\n"
            "nums = [1, 2]\n"
            "nums.append(3)\n"
            "print(nums)\n"
            "Результат: [1, 2, 3]\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. Индексы начинаются с 0.\n"
            "2. Отрицательный индекс идёт с конца.\n"
            "3. Список можно перебирать в цикле for."
        ),
        "tasks": [
            {
                "task": "Создайте список [10, 20, 30] и выведите первый элемент.",
                "example_task": "Создайте список [5, 15, 25] и выведите первый элемент.",
                "example": "nums = [5, 15, 25]\nprint(nums[0])",
                "hint": "Первый элемент имеет индекс 0.",
                "explanation": (
                    "Код решения:\nnums = [10, 20, 30]\nprint(nums[0])\n\n"
                    "Ожидаемый результат: 10"
                ),
                "expected_output": "10",
            },
            {
                "task": "Создайте список ['a', 'b', 'c'] и выведите его длину через len().",
                "example_task": "Создайте список ['x', 'y'] и выведите его длину через len().",
                "example": "letters = ['x', 'y']\nprint(len(letters))",
                "hint": "len(список) возвращает количество элементов.",
                "explanation": (
                    "Код решения:\nletters = ['a', 'b', 'c']\nprint(len(letters))\n\n"
                    "Ожидаемый результат: 3"
                ),
                "expected_output": "3",
            },
        ],
    },
    {
        "title": "Цикл while",
        "theory": (
            "ЦИКЛ WHILE повторяется, пока условие истинно. В отличие "
            "от for, здесь не нужно заранее знать количество повторений.\n\n"

            "ЗАЧЕМ НУЖЕН WHILE\n"
            "for используется, когда знаем число итераций. while — "
            "когда заранее неизвестно, сколько раз нужно повторить "
            "(например, пока пользователь не введёт верный пароль).\n\n"

            "СИНТАКСИС\n"
            "while условие:\n"
            "    тело цикла\n\n"

            "КАК ЭТО РАБОТАЕТ\n"
            "Python проверяет условие:\n"
            "• True → выполняет тело, возвращается к проверке\n"
            "• False → выходит из цикла\n\n"

            "ПРИМЕР 1. Счётчик\n"
            "i = 0\n"
            "while i < 3:\n"
            "    print(i)\n"
            "    i = i + 1\n"
            "Результат: 0, 1, 2\n\n"

            "ПРИМЕР 2. Обратный отсчёт\n"
            "n = 3\n"
            "while n > 0:\n"
            "    print(n)\n"
            "    n = n - 1\n"
            "Результат: 3, 2, 1\n\n"

            "БЕСКОНЕЧНЫЙ ЦИКЛ\n"
            "Если условие никогда не станет False — цикл будет вечным. "
            "Обязательно меняйте переменную внутри цикла!\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. Условие проверяется ПЕРЕД каждой итерацией.\n"
            "2. Нужно менять переменную, иначе цикл не завершится.\n"
            "3. Используйте while, когда число повторений неизвестно."
        ),
        "tasks": [
            {
                "task": "С помощью while выведите числа от 1 до 3.",
                "example_task": "С помощью while выведите числа от 1 до 2.",
                "example": "i = 1\nwhile i <= 2:\n    print(i)\n    i = i + 1",
                "hint": "Начинайте i = 1, цикл пока i <= 3, увеличивайте i на 1.",
                "explanation": (
                    "Код решения:\ni = 1\nwhile i <= 3:\n    print(i)\n    i = i + 1\n\n"
                    "Ожидаемый результат:\n1\n2\n3"
                ),
                "expected_output": "1\n2\n3",
            },
            {
                "task": "С помощью while выведите числа от 5 до 1 в обратном порядке.",
                "example_task": "С помощью while выведите числа от 4 до 1 в обратном порядке.",
                "example": "n = 4\nwhile n >= 1:\n    print(n)\n    n = n - 1",
                "hint": "Начинайте с n = 5, уменьшайте на 1, пока n >= 1.",
                "explanation": (
                    "Код решения:\nn = 5\nwhile n >= 1:\n    print(n)\n    n = n - 1\n\n"
                    "Ожидаемый результат:\n5\n4\n3\n2\n1"
                ),
                "expected_output": "5\n4\n3\n2\n1",
            },
        ],
    },
    {
        "title": "Словари",
        "theory": (
            "СЛОВАРЬ — коллекция пар «ключ: значение». В отличие от "
            "списка, доступ к элементам идёт по ключу, а не по индексу.\n\n"

            "ЗАЧЕМ НУЖНЫ СЛОВАРИ\n"
            "Если нужно связать два значения (например, имя человека "
            "и его возраст) — удобно использовать словарь.\n\n"

            "СОЗДАНИЕ\n"
            "person = {'name': 'Анна', 'age': 25}\n"
            "person = {'имя': 'Иван', 'возраст': 30}\n\n"

            "ДОСТУП К ЗНАЧЕНИЮ\n"
            "person['name']   →  'Анна'\n"
            "person['age']    →  25\n\n"

            "ДОБАВЛЕНИЕ И ИЗМЕНЕНИЕ\n"
            "person['city'] = 'Москва'   # добавить\n"
            "person['age'] = 26           # изменить\n\n"

            "ПОЛЕЗНЫЕ МЕТОДЫ\n"
            "• keys()   — все ключи\n"
            "• values() — все значения\n"
            "• items()  — пары ключ-значение\n\n"

            "ПРИМЕР 1. Доступ\n"
            "d = {'a': 1, 'b': 2}\n"
            "print(d['a'])\n"
            "Результат: 1\n\n"

            "ПРИМЕР 2. Перебор\n"
            "for key in {'x': 1, 'y': 2}:\n"
            "    print(key)\n"
            "Результат: x, y\n\n"

            "ПРИМЕР 3. Сумма значений\n"
            "d = {'x': 10, 'y': 20}\n"
            "print(d['x'] + d['y'])\n"
            "Результат: 30\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. Ключи уникальны — повторение перезапишет значение.\n"
            "2. Ключом может быть строка или число.\n"
            "3. Порядок в словаре не важен."
        ),
        "tasks": [
            {
                "task": "Создайте словарь {'a': 1} и выведите значение по ключу 'a'.",
                "example_task": "Создайте словарь {'x': 5} и выведите значение по ключу 'x'.",
                "example": "d = {'x': 5}\nprint(d['x'])",
                "hint": "Доступ к значению — через квадратные скобки и ключ.",
                "explanation": (
                    "Код решения:\nd = {'a': 1}\nprint(d['a'])\n\n"
                    "Ожидаемый результат: 1"
                ),
                "expected_output": "1",
            },
            {
                "task": "Создайте {'x': 10, 'y': 20} и выведите сумму значений.",
                "example_task": "Создайте {'x': 5, 'y': 15} и выведите сумму значений.",
                "example": "d = {'x': 5, 'y': 15}\nprint(d['x'] + d['y'])",
                "hint": "Сложите d['x'] и d['y'].",
                "explanation": (
                    "Код решения:\nd = {'x': 10, 'y': 20}\nprint(d['x'] + d['y'])\n\n"
                    "Ожидаемый результат: 30"
                ),
                "expected_output": "30",
            },
        ],
    },
    {
        "title": "Строки",
        "theory": (
            "СТРОКА — последовательность символов в кавычках. У строк "
            "есть много встроенных методов.\n\n"

            "СОЗДАНИЕ\n"
            "s1 = 'Привет'\n"
            "s2 = \"Мир\"\n"
            "s3 = 'Много\\nстрок'\n\n"

            "ОСНОВНЫЕ ОПЕРАЦИИ\n"
            "• s.upper()   — в верхний регистр\n"
            "• s.lower()   — в нижний регистр\n"
            "• s.strip()   — убрать пробелы по краям\n"
            "• s.replace(a, b) — заменить\n"
            "• s.split(sep)    — разбить по разделителю\n"
            "• len(s)      — длина строки\n\n"

            "ИНДЕКСЫ И СРЕЗЫ\n"
            "s = 'Python'\n"
            "s[0]     → 'P'\n"
            "s[-1]    → 'n'\n"
            "s[0:3]   → 'Pyt'\n\n"

            "F-СТРОКИ\n"
            "name = 'Анна'\n"
            "age = 25\n"
            "print(f'{name} — {age} лет')\n"
            "Результат: Анна — 25 лет\n\n"

            "ПРИМЕР 1. Методы\n"
            "s = '  Hello  '\n"
            "print(s.strip())\n"
            "print(s.upper())\n"
            "Результат: 'Hello', '  HELLO  '\n\n"

            "ПРИМЕР 2. F-строка\n"
            "x = 5\n"
            "print(f'x = {x}')\n"
            "Результат: x = 5\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. Строки неизменяемы — методы возвращают новую строку.\n"
            "2. Индексация с 0, срез [start:end] не включает end.\n"
            "3. F-строки — самый удобный способ подставить значения."
        ),
        "tasks": [
            {
                "task": "Дана строка s = 'hello'. Выведите её в верхнем регистре.",
                "example_task": "Дана строка s = 'world'. Выведите её в верхнем регистре.",
                "example": "s = 'world'\nprint(s.upper())",
                "hint": "Метод .upper() возвращает строку в верхнем регистре.",
                "explanation": (
                    "Код решения:\ns = 'hello'\nprint(s.upper())\n\n"
                    "Ожидаемый результат: HELLO"
                ),
                "expected_output": "HELLO",
            },
            {
                "task": "Дано name = 'Иван'. Выведите 'Привет, Иван!' через f-строку.",
                "example_task": "Дано name = 'Анна'. Выведите 'Привет, Анна!' через f-строку.",
                "example": "name = 'Анна'\nprint(f'Привет, {name}!')",
                "hint": "Перед строкой поставьте f, значение вставляйте в {}.",
                "explanation": (
                    "Код решения:\nname = 'Иван'\nprint(f'Привет, {name}!')\n\n"
                    "Ожидаемый результат: Привет, Иван!"
                ),
                "expected_output": "Привет, Иван!",
            },
        ],
    },
    {
        "title": "Исключения",
        "theory": (
            "ИСКЛЮЧЕНИЕ — это ошибка, которая возникает во время работы "
            "программы. Их можно перехватывать и обрабатывать.\n\n"

            "ЗАЧЕМ НУЖНЫ ИСКЛЮЧЕНИЯ\n"
            "Программа не должна падать при ошибке. Например, если "
            "пользователь ввёл текст вместо числа — нужно вежливо "
            "сообщить, а не вылетать.\n\n"

            "СИНТАКСИС\n"
            "try:\n"
            "    код_который_может_упасть\n"
            "except ТипОшибки:\n"
            "    что_делать_при_ошибке\n"
            "else:\n"
            "    если_ошибки_не_было\n"
            "finally:\n"
            "    выполнится_в_любом_случае\n\n"

            "ТИПЫ ОШИБОК\n"
            "• ZeroDivisionError — деление на ноль\n"
            "• ValueError — неверное значение\n"
            "• TypeError — неверный тип\n"
            "• KeyError — нет ключа в словаре\n"
            "• IndexError — индекс вне списка\n\n"

            "ПРИМЕР 1. Деление\n"
            "try:\n"
            "    print(10 / 0)\n"
            "except ZeroDivisionError:\n"
            "    print('Деление на ноль!')\n\n"

            "ПРИМЕР 2. Сообщение об ошибке\n"
            "try:\n"
            "    x = int('abc')\n"
            "except ValueError as e:\n"
            "    print(f'Ошибка: {e}')\n\n"

            "ПРИМЕР 3. С finally\n"
            "try:\n"
            "    x = 5 / 1\n"
            "except ZeroDivisionError:\n"
            "    print('ошибка')\n"
            "finally:\n"
            "    print('всё равно выполнится')\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. try-блок — опасный код, except — обработка.\n"
            "2. Ошибки не падают насовсем — их можно поймать.\n"
            "3. Лучше указывать конкретный тип ошибки."
        ),
        "tasks": [
            {
                "task": "Обработайте 10 / 0 через try/except и выведите 'error'.",
                "example_task": "Обработайте 5 / 0 через try/except и выведите 'err'.",
                "example": "try:\n    print(5 / 0)\nexcept ZeroDivisionError:\n    print('err')",
                "hint": "Деление на ноль вызывает ZeroDivisionError.",
                "explanation": (
                    "Код решения:\ntry:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print('error')\n\n"
                    "Ожидаемый результат: error"
                ),
                "expected_output": "error",
            },
            {
                "task": "Обработайте int('abc') через try/except и выведите 'fail'.",
                "example_task": "Обработайте int('xyz') через try/except и выведите 'no'.",
                "example": "try:\n    x = int('xyz')\nexcept ValueError:\n    print('no')",
                "hint": "Преобразование не-числа в int вызывает ValueError.",
                "explanation": (
                    "Код решения:\ntry:\n    x = int('abc')\nexcept ValueError:\n    print('fail')\n\n"
                    "Ожидаемый результат: fail"
                ),
                "expected_output": "fail",
            },
        ],
    },
    {
        "title": "Мини-проект: Калькулятор",
        "theory": (
            "Соберём вместе всё, что изучили: переменные, арифметику, "
            "функции, вывод.\n\n"

            "ЧТО ДЕЛАЕМ\n"
            "Напишем несколько функций для арифметических операций: "
            "сложение, вычитание, умножение и деление.\n\n"

            "ПРИМЕР\n"
            "def add(a, b):\n"
            "    return a + b\n"
            "print(add(2, 3))   →  5\n\n"

            "ПРИМЕР 2. Вычитание\n"
            "def sub(a, b):\n"
            "    return a - b\n"
            "print(sub(10, 4))   →  6\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. Функция возвращает результат через return.\n"
            "2. Аргументы передаются в скобках при вызове.\n"
            "3. Имя функции должно отражать её действие."
        ),
        "tasks": [
            {
                "task": "Напишите функцию add(a, b) и выведите результат add(7, 8).",
                "example_task": "Напишите функцию add(a, b) и выведите результат add(2, 3).",
                "example": "def add(a, b):\n    return a + b\nprint(add(2, 3))",
                "hint": "Функция с двумя параметрами и возвратом через return.",
                "explanation": (
                    "Код решения:\ndef add(a, b):\n    return a + b\nprint(add(7, 8))\n\n"
                    "Ожидаемый результат: 15"
                ),
                "expected_output": "15",
            },
            {
                "task": "Напишите функцию sub(a, b) и выведите sub(20, 8).",
                "example_task": "Напишите функцию sub(a, b) и выведите sub(10, 4).",
                "example": "def sub(a, b):\n    return a - b\nprint(sub(10, 4))",
                "hint": "Разность — это a - b.",
                "explanation": (
                    "Код решения:\ndef sub(a, b):\n    return a - b\nprint(sub(20, 8))\n\n"
                    "Ожидаемый результат: 12"
                ),
                "expected_output": "12",
            },
        ],
    },
    {
        "title": "Мини-проект: Модули",
        "theory": (
            "МОДУЛЬ — это файл с кодом, который можно подключить к "
            "своей программе. В Python сотни встроенных модулей.\n\n"

            "СИНТАКСИС ИМПОРТА\n"
            "import math                 # весь модуль\n"
            "from math import sqrt       # конкретная функция\n"
            "import math as m            # переименовать\n\n"

            "ПОЛЕЗНЫЕ МОДУЛИ\n"
            "• math — математика (sqrt, pi, sin)\n"
            "• random — случайные числа\n"
            "• datetime — дата и время\n"
            "• os — работа с файлами\n\n"

            "ПРИМЕР 1. math\n"
            "import math\n"
            "print(math.sqrt(16))   → 4.0\n\n"

            "ПРИМЕР 2. random\n"
            "import random\n"
            "n = random.randint(1, 10)\n"
            "print(n)   → случайное число от 1 до 10\n\n"

            "ПРИМЕР 3. Из модуля напрямую\n"
            "from math import pi\n"
            "print(pi)   → 3.141592653589793\n\n"

            "ВАЖНО ЗАПОМНИТЬ\n"
            "1. import ставится в начале файла.\n"
            "2. Можно импортировать функции по одной.\n"
            "3. Свой модуль — это просто .py файл."
        ),
        "tasks": [
            {
                "task": "Импортируйте math и выведите math.sqrt(25).",
                "example_task": "Импортируйте math и выведите math.sqrt(16).",
                "example": "import math\nprint(math.sqrt(16))",
                "hint": "sqrt — квадратный корень.",
                "explanation": (
                    "Код решения:\nimport math\nprint(math.sqrt(25))\n\n"
                    "Ожидаемый результат: 5.0"
                ),
                "expected_output": "5.0",
            },
            {
                "task": "Импортируйте pi из math и выведите round(pi, 2).",
                "example_task": "Импортируйте pi из math и выведите round(pi, 3).",
                "example": "from math import pi\nprint(round(pi, 3))",
                "hint": "from math import pi — берём только pi.",
                "explanation": (
                    "Код решения:\nfrom math import pi\nprint(round(pi, 2))\n\n"
                    "Ожидаемый результат: 3.14"
                ),
                "expected_output": "3.14",
            },
        ],
    },
]


# ============ Главный класс ============
class LearnPythonApp(toga.App):

    def startup(self):
        self.current_lesson_index = 0
        self.current_task_index = 0
        self.achievements_unlocked = set()
        self._init_db()
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.build_lesson_list_screen()
        self.main_window.show()

    # ---------- БД ----------
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
        cur.execute("""
            CREATE TABLE IF NOT EXISTS achievements (
                key TEXT PRIMARY KEY,
                unlocked_at TEXT
            )
        """)
        self.db.commit()
        cur.execute("SELECT key FROM achievements")
        self.achievements_unlocked = {row[0] for row in cur.fetchall()}

    def mark_completed(self, lesson_idx, task_idx):
        cur = self.db.cursor()
        cur.execute("INSERT OR REPLACE INTO completed VALUES (?, ?, ?)",
                    (lesson_idx, task_idx, datetime.now().isoformat()))
        self.db.commit()
        self._check_achievements()

    def is_completed(self, lesson_idx, task_idx):
        cur = self.db.cursor()
        cur.execute("SELECT 1 FROM completed WHERE lesson_idx=? AND task_idx=?",
                    (lesson_idx, task_idx))
        return cur.fetchone() is not None

    def count_completed(self, lesson_idx):
        cur = self.db.cursor()
        cur.execute("SELECT COUNT(*) FROM completed WHERE lesson_idx=?",
                    (lesson_idx,))
        return cur.fetchone()[0]

    def total_completed(self):
        return sum(self.count_completed(i) for i in range(len(LESSONS)))

    def total_tasks(self):
        return sum(len(l["tasks"]) for l in LESSONS)

    def _unlock_achievement(self, key):
        if key in self.achievements_unlocked:
            return
        self.achievements_unlocked.add(key)
        cur = self.db.cursor()
        cur.execute("INSERT OR REPLACE INTO achievements VALUES (?, ?)",
                    (key, datetime.now().isoformat()))
        self.db.commit()
        try:
            self.main_window.info_dialog("Новое достижение!", ACHIEVEMENTS[key])
        except Exception:
            pass

    def _check_achievements(self):
        total_done = self.total_completed()
        total_all = self.total_tasks()
        if total_done >= 1:
            self._unlock_achievement("first_step")
        if total_all > 0 and total_done >= total_all / 2:
            self._unlock_achievement("half_way")
        if all(self.count_completed(i) == len(LESSONS[i]["tasks"])
               for i in [1, 5]):
            self._unlock_achievement("cycle_master")
        if self.count_completed(2) == len(LESSONS[2]["tasks"]):
            self._unlock_achievement("function_guru")
        if total_done == total_all:
            self._unlock_achievement("all_done")

    # ---------- Экран 1 ----------
    def build_lesson_list_screen(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=12, flex=1))

        title = toga.Label(
            "🐍 Уроки Python",
            style=Pack(font_size=22, font_weight="bold",
                       margin_bottom=6, text_align=CENTER),
        )
        main_box.add(title)

        done = self.total_completed()
        total = self.total_tasks()
        fraction = (done / total) if total else 0.0

        progress_label = toga.Label(
            f"Прогресс: {done} из {total}",
            style=Pack(font_size=13, margin_bottom=4, text_align=CENTER),
        )
        main_box.add(progress_label)

        try:
            self._progress_bar = toga.ProgressBar(max=1.0, value=fraction,
                                                  style=Pack(margin=5))
            main_box.add(self._progress_bar)
        except Exception:
            pass

        next_lesson = self._find_next_lesson()
        if next_lesson is not None:
            cont_btn = toga.Button(
                "Продолжить обучение",
                on_press=self._open_next,
                style=BTN_ACCENT_STYLE,
            )
            cont_btn.lesson_index = next_lesson
            main_box.add(cont_btn)

        lessons_box = toga.Box(style=Pack(direction=COLUMN))
        scroll = toga.ScrollContainer(
            content=lessons_box, style=Pack(flex=1), horizontal=False,
        )

        for idx, lesson in enumerate(LESSONS):
            cnt = self.count_completed(idx)
            total_l = len(lesson["tasks"])
            is_done = (cnt == total_l)

            if is_done:
                label = f"{idx + 1}. {lesson['title']}"
                style = Pack(margin=4, background_color=BTN_SUCCESS)
            elif cnt > 0:
                label = f"{idx + 1}. {lesson['title']}  ({cnt}/{total_l})"
                style = BTN_STYLE
            else:
                label = f"{idx + 1}. {lesson['title']}"
                style = BTN_STYLE

            btn = toga.Button(label, on_press=self.open_lesson, style=style)
            btn.lesson_index = idx
            lessons_box.add(btn)

        main_box.add(scroll)

        sandbox_btn = toga.Button(
            "Свободный код",
            on_press=self.open_sandbox,
            style=Pack(margin=5, background_color=BTN_ACCENT),
        )
        main_box.add(sandbox_btn)

        reset_btn = toga.Button(
            "Сбросить прогресс",
            on_press=self.confirm_reset,
            style=BTN_STYLE,
        )
        main_box.add(reset_btn)

        return main_box

    def _find_next_lesson(self):
        for idx, lesson in enumerate(LESSONS):
            if self.count_completed(idx) < len(lesson["tasks"]):
                return idx
        return None

    def _open_next(self, widget):
        self.open_lesson(widget)

    def confirm_reset(self, widget):
        def _do_reset(w, result):
            if not result:
                return
            cur = self.db.cursor()
            cur.execute("DELETE FROM completed")
            cur.execute("DELETE FROM achievements")
            self.db.commit()
            self.achievements_unlocked = set()
            self.main_window.content = self.build_lesson_list_screen()

        try:
            self.main_window.confirm_dialog(
                "Сброс прогресса",
                "Вы уверены? Все выполненные задачи будут удалены. "
                "Действие необратимо.",
                on_result=_do_reset,
            )
        except Exception:
            cur = self.db.cursor()
            cur.execute("DELETE FROM completed")
            cur.execute("DELETE FROM achievements")
            self.db.commit()
            self.achievements_unlocked = set()
            self.main_window.content = self.build_lesson_list_screen()

    # ---------- Экран 2: теория ----------
    def open_lesson(self, widget):
        self.current_lesson_index = getattr(widget, "lesson_index",
                                            self.current_lesson_index)
        lesson = LESSONS[self.current_lesson_index]

        main_box = toga.Box(style=Pack(direction=COLUMN, margin=10, flex=1))

        practice_btn = toga.Button(
            "Перейти к практике",
            on_press=self.open_practice_screen,
            style=BTN_MAIN_STYLE,
        )
        main_box.add(practice_btn)

        self.theory_view = toga.MultilineTextInput(
            readonly=True,
            value=lesson["theory"],
            style=Pack(flex=1, margin=5),
        )
        main_box.add(self.theory_view)

        back_btn = toga.Button(
            "← Назад к списку",
            on_press=self.go_back_to_list,
            style=BTN_STYLE,
        )
        main_box.add(back_btn)

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

        main_box = toga.Box(style=Pack(direction=COLUMN, margin=8, flex=1))

        # Переключатель задач — активная РОЗОВАЯ, неактивная ФИОЛЕТОВАЯ
        if len(lesson["tasks"]) > 1:
            switch_row = toga.Box(style=Pack(direction=ROW, margin=4))
            for idx, t in enumerate(lesson["tasks"]):
                label = f"Задача {idx + 1}"
                if idx == self.current_task_index:
                    btn_color = BTN_PRIMARY      # розовая — активная
                else:
                    btn_color = BTN_SECONDARY    # фиолетовая — неактивная
                btn = toga.Button(
                    label,
                    on_press=self.switch_task,
                    style=Pack(flex=1, margin_left=2, margin_right=2,
                               background_color=btn_color),
                )
                btn.task_index = idx
                switch_row.add(btn)
            main_box.add(switch_row)

        # Условие задачи
        task_header = toga.Label(
            "Условие задачи:",
            style=Pack(font_size=13, font_weight="bold",
                       margin_left=5, margin_top=4),
        )
        main_box.add(task_header)

        task_text = toga.MultilineTextInput(
            readonly=True,
            value=task["task"],
            style=Pack(flex=1, margin=4),
        )
        main_box.add(task_text)

        # Пример — увеличен (flex=3)
        example_header = toga.Label(
            "Пример:",
            style=Pack(font_size=13, font_weight="bold",
                       margin_left=5, margin_top=4),
        )
        main_box.add(example_header)

        example_block = (
            task.get("example_task", "") + "\n\n" +
            task.get("example", "")
        )
        example_text = toga.MultilineTextInput(
            readonly=True,
            value=example_block,
            style=Pack(flex=3, margin=4),
        )
        main_box.add(example_text)

        # Ввод кода
        input_header = toga.Label(
            "Введите ваш код:",
            style=Pack(font_size=13, font_weight="bold",
                       margin_left=5, margin_top=4),
        )
        main_box.add(input_header)

        self.code_editor = toga.MultilineTextInput(
            placeholder="Здесь пишите ваш код...",
            style=Pack(flex=4, margin=4),
        )
        main_box.add(self.code_editor)

        run_btn = toga.Button(
            "Запустить",
            on_press=self.run_code,
            style=Pack(flex=1, margin=3, background_color=BTN_SECONDARY),
        )
        check_btn = toga.Button(
            "✅ Проверить",
            on_press=self.check_answer,
            style=Pack(flex=1, margin=3, background_color=BTN_SECONDARY),
        )
        row1 = toga.Box(style=Pack(direction=ROW, margin=2))
        row1.add(run_btn)
        row1.add(check_btn)
        main_box.add(row1)

        clear_btn = toga.Button(
            "Сбросить код",
            on_press=self.clear_code,
            style=Pack(flex=1, margin=3, background_color=BTN_SECONDARY),
        )
        hint_btn = toga.Button(
            "Подсказка",
            on_press=self.show_hint,
            style=Pack(flex=1, margin=3, background_color=BTN_ACCENT),
        )
        row2 = toga.Box(style=Pack(direction=ROW, margin=2))
        row2.add(clear_btn)
        row2.add(hint_btn)
        main_box.add(row2)

        explain_btn = toga.Button(
            "Показать разбор",
            on_press=self.show_explanation,
            style=Pack(margin=3, background_color=BTN_PRIMARY),
        )
        main_box.add(explain_btn)

        back_btn = toga.Button(
            "Назад к теории",
            on_press=self.go_back_to_theory,
            style=Pack(margin=3, background_color=BTN_SECONDARY),
        )
        main_box.add(back_btn)

        # Результат — уменьшен (flex=1)
        result_header = toga.Label(
            "Результат выполнения:",
            style=Pack(font_size=13, font_weight="bold",
                       margin_left=5, margin_top=4),
        )
        main_box.add(result_header)

        self.output_text = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=1, margin=4),
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

    def clear_code(self, widget):
        self.code_editor.value = ""

    def show_hint(self, widget):
        task = LESSONS[self.current_lesson_index]["tasks"][self.current_task_index]
        self.output_text.value = "Подсказка:\n" + task.get("hint", "—")

    # ---------- Песочница ----------
    def open_sandbox(self, widget):
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=10, flex=1))

        title = toga.Label(
            "Свободный код",
            style=Pack(font_size=18, font_weight="bold",
                       margin_bottom=6, text_align=CENTER),
        )
        main_box.add(title)

        tpl_row = toga.Box(style=Pack(direction=ROW, margin=4))
        for name, code in [
            ("print", "print('Привет!')"),
            ("for", "for i in range(3):\n    print(i)"),
            ("if", "x = 5\nif x > 3:\n    print('больше')"),
        ]:
            b = toga.Button(name, on_press=self._apply_template,
                            style=Pack(flex=1, margin=2,
                                       background_color=BTN_SECONDARY))
            b.template_code = code
            tpl_row.add(b)
        main_box.add(tpl_row)

        self.sandbox_editor = toga.MultilineTextInput(
            placeholder="Введите любой код...",
            style=Pack(flex=3, margin=4),
        )
        main_box.add(self.sandbox_editor)

        row = toga.Box(style=Pack(direction=ROW, margin=4))
        run_btn = toga.Button("Запустить", on_press=self.run_sandbox,
                              style=Pack(flex=1, margin=2,
                                         background_color=BTN_PRIMARY))
        clear_btn = toga.Button("Очистить", on_press=self.clear_sandbox,
                                style=Pack(flex=1, margin=2,
                                           background_color=BTN_SECONDARY))
        row.add(run_btn)
        row.add(clear_btn)
        main_box.add(row)

        back_btn = toga.Button("Назад к списку", on_press=self.go_back_to_list,
                               style=Pack(margin=4,
                                          background_color=BTN_SECONDARY))
        main_box.add(back_btn)

        self.sandbox_output = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=2, margin=4),
        )
        main_box.add(self.sandbox_output)

        self.main_window.content = main_box

    def _apply_template(self, widget):
        self.sandbox_editor.value = getattr(widget, "template_code", "")

    def run_sandbox(self, widget):
        code = self.sandbox_editor.value
        error, output = self.execute_code(code)
        if error:
            self.sandbox_output.value = f"Ошибка:\n{error}"
        else:
            self.sandbox_output.value = output if output else "(нет вывода)"

    def clear_sandbox(self, widget):
        self.sandbox_editor.value = ""
        self.sandbox_output.value = ""

    # ---------- Выполнение кода ----------
    def execute_code(self, code):
        buf = io.StringIO()
        error = None
        line_count = [0]
        MAX_LINES = 500_000

        def tracer(frame, event, arg):
            if event == "line":
                line_count[0] += 1
                if line_count[0] > MAX_LINES:
                    raise TimeoutError(
                        "превышено время выполнения (бесконечный цикл?)"
                    )
            return tracer

        try:
            sys.settrace(tracer)
            with redirect_stdout(buf):
                exec(code, {})
        except SyntaxError as e:
            error = f"Синтаксическая ошибка: {e.msg} (строка {e.lineno})"
        except NameError as e:
            error = f"Имя не определено: {e}"
        except ZeroDivisionError:
            error = "Деление на ноль"
        except TypeError as e:
            error = f"Ошибка типа: {e}"
        except IndexError as e:
            error = f"Индекс вне диапазона: {e}"
        except KeyError as e:
            error = f"Ключ не найден: {e}"
        except TimeoutError as e:
            error = str(e)
        except Exception as e:
            error = f"{type(e).__name__}: {e}"
        finally:
            sys.settrace(None)

        return error, buf.getvalue()

    def run_code(self, widget):
        code = self.code_editor.value
        if not code.strip():
            self.output_text.value = "Сначала введите код."
            return
        error, output = self.execute_code(code)
        if error:
            self.output_text.value = f"Ошибка:\n{error}"
        else:
            self.output_text.value = output if output.strip() else "(нет вывода)"

    def show_explanation(self, widget):
        task = LESSONS[self.current_lesson_index]["tasks"][self.current_task_index]
        self.output_text.value = task["explanation"]

    def check_answer(self, widget):
        code = self.code_editor.value
        if not code.strip():
            self.output_text.value = "Сначала введите код."
            return

        error, user_output = self.execute_code(code)

        if error:
            self.output_text.value = f"Ошибка при выполнении:\n{error}"
            return

        user_output = user_output.strip()
        task = LESSONS[self.current_lesson_index]["tasks"][self.current_task_index]
        expected = task["expected_output"].strip()

        if user_output == expected:
            self.mark_completed(self.current_lesson_index, self.current_task_index)
            self.output_text.value = (
                "Верно! Отличная работа.\n\n"
                "Прогресс сохранён."
            )
        else:
            self.output_text.value = (
                f"Не совсем.\n\n"
                f"Ожидалось:\n{expected}\n\n"
                f"Ваш вывод:\n{user_output if user_output else '(пусто)'}"
            )


def main():
    return LearnPythonApp()
