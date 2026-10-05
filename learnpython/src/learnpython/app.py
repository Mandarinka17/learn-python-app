"""
Приложение для изучения основ Python
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
import sys
import io


BTN_PINK = "#F8BBD0"
BTN_PINK_DARK = "#F06292"

BTN_STYLE = Pack(margin=5, background_color=BTN_PINK)
BTN_MAIN_STYLE = Pack(margin=5, background_color=BTN_PINK_DARK)


LESSONS = [
    {
        "title": "Урок 1: Переменные",
        "theory": (
            "ПЕРЕМЕННАЯ — это именованный контейнер для хранения данных. "
            "Когда вы пишете «x = 5», вы создаёте переменную x, которая "
            "хранит число 5. Переменная — это как коробка с наклейкой: "
            "на наклейке написано имя, а внутри лежит значение.\n\n"

            "📌 ЗАЧЕМ НУЖНЫ ПЕРЕМЕННЫЕ\n"
            "Программа — это последовательность операций с данными. "
            "Чтобы эти данные где-то хранить и повторно использовать, "
            "придумали переменные. Вместо того чтобы каждый раз писать "
            "число 25, вы пишете age — и Python подставляет значение.\n\n"

            "📌 КАК СОЗДАТЬ ПЕРЕМЕННУЮ\n"
            "В Python переменная создаётся в момент присваивания:\n"
            "name = 'Анна'\n"
            "Здесь name — имя переменной, = — оператор присваивания, "
            "'Анна' — значение. После этой строки Python запоминает: "
            "«переменная name содержит строку Анна».\n\n"

            "📌 ПРАВИЛА ИМЕНОВАНИЯ\n"
            "• Имя может содержать латинские и русские буквы, цифры, _\n"
            "• Имя НЕ может начинаться с цифры: 5x — ошибка, x5 — ок\n"
            "• Нельзя использовать пробелы и знаки препинания\n"
            "• Регистр важен: name и Name — это РАЗНЫЕ переменные\n"
            "• Нельзя называть переменную служебным словом\n"
            "  (print, for, if, while и т.д.)\n"
            "• Имя должно быть осмысленным: age лучше, чем a\n\n"

            "📌 ТИПЫ ДАННЫХ\n"
            "Python — язык с динамической типизацией. Это значит, что "
            "вам НЕ нужно указывать тип переменной — Python сам "
            "определяет его по значению.\n\n"
            "Основные типы:\n"
            "• int — целые числа: 5, -10, 100, 2024\n"
            "• float — дробные числа: 3.14, 2.5, -0.7\n"
            "• str — строки в кавычках: 'Анна', \"Привет\"\n"
            "• bool — логические значения: True или False\n\n"

            "📌 ПРИМЕР 1. Числа и строки\n"
            "name = 'Анна'\n"
            "age = 25\n"
            "print(name)\n"
            "print(age)\n\n"
            "Результат:\n"
            "Анна\n"
            "25\n\n"

            "📌 ПРИМЕР 2. Операции с переменными\n"
            "x = 10\n"
            "y = 3\n"
            "print(x + y)   →  13\n"
            "print(x * y)   →  30\n"
            "print(x - y)   →  7\n"
            "print(x / y)   →  3.333...\n\n"

            "📌 ФУНКЦИЯ print()\n"
            "print() — это встроенная функция вывода на экран. "
            "Внутри скобок пишется то, что нужно вывести. "
            "Можно выводить значения переменных, числа, строки, "
            "а также их комбинации через запятую:\n"
            "print('Возраст:', age)\n"
            "Результат: Возраст: 25\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Переменная создаётся в момент присваивания через =.\n"
            "2. Тип данных Python определяет автоматически.\n"
            "3. Одно и то же имя можно перезаписать новым значением.\n"
            "4. print() нужен для того, чтобы увидеть результат."
        ),
        "tasks": [
            {
                "task": "Создайте переменную со значением 7 и выведите её на экран.",
                "example": "number = 7\nprint(number)",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "1. Создать переменную и положить в неё число 7\n"
                    "2. Вывести значение на экран\n\n"
                    "Код решения:\n"
                    "number = 7\n"
                    "print(number)\n\n"
                    "Пошагово:\n"
                    "• number = 7 — создаём переменную, кладём число 7\n"
                    "• print(number) — выводим то, что в ней хранится\n\n"
                    "Ожидаемый результат: 7"
                ),
                "expected_output": "7",
            },
            {
                "task": "Создайте переменные a = 6 и b = 4. Выведите их сумму и произведение.",
                "example": "a = 6\nb = 4\nprint(a + b)\nprint(a * b)",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "1. Создать переменную a = 6\n"
                    "2. Создать переменную b = 4\n"
                    "3. Вывести сумму a + b\n"
                    "4. Вывести произведение a * b\n\n"
                    "Код решения:\n"
                    "a = 6\n"
                    "b = 4\n"
                    "print(a + b)\n"
                    "print(a * b)\n\n"
                    "Пошагово:\n"
                    "• a = 6 и b = 4 — две числовые переменные\n"
                    "• print(a + b) выводит 10\n"
                    "• print(a * b) выводит 24\n\n"
                    "Ожидаемый результат:\n10\n24"
                ),
                "expected_output": "10\n24",
            },
        ],
    },
    {
        "title": "Урок 2: Цикл for",
        "theory": (
            "ЦИКЛ — это конструкция, которая повторяет блок кода "
            "несколько раз. Цикл for используется, когда заранее "
            "известно, сколько раз нужно повторить действие.\n\n"

            "📌 ЗАЧЕМ НУЖНЫ ЦИКЛЫ\n"
            "Представьте, что нужно вывести на экран числа от 1 до 100. "
            "Можно написать 100 строк print() — а можно 2 строки "
            "с циклом. Циклы делают программы в десятки раз короче "
            "и понятнее. Это одна из главных идей программирования.\n\n"

            "📌 СИНТАКСИС ЦИКЛА for\n"
            "for переменная in последовательность:\n"
            "    тело цикла\n\n"
            "Разбор:\n"
            "• for — ключевое слово, начало цикла\n"
            "• переменная — имя, которое принимает значения\n"
            "• in — ключевое слово\n"
            "• последовательность — откуда берутся значения\n"
            "• двоеточие в конце строки обязательно\n"
            "• тело цикла — с отступом в 4 пробела\n\n"

            "📌 КАК РАБОТАЕТ ЦИКЛ\n"
            "Python по очереди берёт значения из последовательности, "
            "кладёт в переменную и выполняет тело цикла. "
            "Когда значения заканчиваются — цикл завершается.\n\n"

            "📌 ФУНКЦИЯ range()\n"
            "range() создаёт последовательность чисел.\n"
            "У неё три формы вызова:\n\n"
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

            "📌 ПРИМЕР 1. Простой цикл\n"
            "for i in range(3):\n"
            "    print(i)\n\n"
            "Пошагово:\n"
            "1. range(3) создаёт значения 0, 1, 2\n"
            "2. i = 0 → print выводит 0\n"
            "3. i = 1 → print выводит 1\n"
            "4. i = 2 → print выводит 2\n"
            "5. Значения закончились, цикл завершён\n\n"

            "📌 ПРИМЕР 2. Цикл по строке\n"
            "word = 'Python'\n"
            "for letter in word:\n"
            "    print(letter)\n\n"
            "Python выводит по одной букве: P, y, t, h, o, n.\n"
            "Строка — это тоже последовательность символов.\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Тело цикла выделяется ОТСТУПОМ в 4 пробела.\n"
            "2. Без отступа Python выдаст ошибку.\n"
            "3. Имя переменной цикла может быть любым (i, j, x).\n"
            "4. Все действия с отступом выполняются на каждой итерации."
        ),
        "tasks": [
            {
                "task": "Выведите числа от 0 до 4 с помощью цикла for.",
                "example": "for i in range(5):\n    print(i)",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "Вывести пять чисел: 0, 1, 2, 3, 4 — каждое с новой строки.\n\n"
                    "Код решения:\n"
                    "for i in range(5):\n"
                    "    print(i)\n\n"
                    "Пошагово:\n"
                    "• range(5) создаёт последовательность 0, 1, 2, 3, 4\n"
                    "• i по очереди принимает каждое значение\n"
                    "• print(i) выводит текущее значение\n\n"
                    "ВАЖНО: отступ перед print() — 4 пробела!\n\n"
                    "Ожидаемый результат:\n0\n1\n2\n3\n4"
                ),
                "expected_output": "0\n1\n2\n3\n4",
            },
            {
                "task": "Выведите буквы слова 'Кот' с помощью цикла for (каждую с новой строки).",
                "example": "word = 'Кот'\nfor letter in word:\n    print(letter)",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "Вывести буквы К, о, т — каждую на своей строке.\n\n"
                    "Код решения:\n"
                    "word = 'Кот'\n"
                    "for letter in word:\n"
                    "    print(letter)\n\n"
                    "Пошагово:\n"
                    "• word = 'Кот' — переменная со строкой\n"
                    "• for letter in word — цикл проходит по каждой букве\n"
                    "• print(letter) выводит текущую букву\n\n"
                    "Ожидаемый результат:\nК\nо\nт"
                ),
                "expected_output": "К\nо\nт",
            },
        ],
    },
    {
        "title": "Урок 3: Функции",
        "theory": (
            "ФУНКЦИЯ — это блок кода, который можно вызывать "
            "многократно по имени. Функции делают программу "
            "короче, понятнее и удобнее для повторного использования.\n\n"

            "📌 ЗАЧЕМ НУЖНЫ ФУНКЦИИ\n"
            "Представьте, что в программе нужно 10 раз посчитать "
            "площадь прямоугольника. Можно 10 раз написать формулу — "
            "а можно один раз создать функцию и вызывать её. "
            "Если формула изменится — править придётся в одном месте.\n\n"

            "📌 СИНТАКСИС ОБЪЯВЛЕНИЯ\n"
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

            "📌 КЛЮЧЕВОЕ СЛОВО return\n"
            "return выполняет две роли:\n"
            "1. Возвращает значение туда, откуда вызвали функцию\n"
            "2. Завершает выполнение функции\n\n"
            "Если не написать return — функция вернёт None.\n\n"

            "📌 ОБЪЯВЛЕНИЕ И ВЫЗОВ — ЭТО РАЗНОЕ\n"
            "Объявление функции — это её описание:\n"
            "def square(x):\n"
            "    return x * x\n\n"
            "После объявления функция НИЧЕГО не делает. "
            "Чтобы она сработала, её нужно ВЫЗВАТЬ:\n"
            "print(square(4))   →  16\n\n"
            "Вызов — это имя функции со скобками и аргументами.\n\n"

            "📌 ПРИМЕР 1. Функция с возвратом\n"
            "def square(x):\n"
            "    return x * x\n"
            "print(square(4))\n\n"
            "Пошагово:\n"
            "1. square(4) — вызываем функцию, x = 4\n"
            "2. Внутри: return 4 * 4 → 16\n"
            "3. Функция возвращает 16\n"
            "4. print выводит 16\n\n"

            "📌 ПРИМЕР 2. Функция с двумя параметрами\n"
            "def greet(name, age):\n"
            "    return f'Привет, {name}! Тебе {age} лет.'\n"
            "print(greet('Анна', 25))\n\n"
            "Функция принимает два параметра и возвращает строку. "
            "F-строка (f'...') — это удобный способ вставить "
            "значение переменной прямо в текст.\n\n"

            "📌 ПАРАМЕТРЫ И АРГУМЕНТЫ\n"
            "Параметры — это имена внутри объявления функции.\n"
            "Аргументы — это конкретные значения при вызове.\n"
            "def add(a, b):    ← a и b это параметры\n"
            "add(3, 5)         ← 3 и 5 это аргументы\n\n"

            "📌 ВАЖНО ЗАПОМНИТЬ\n"
            "1. Функция сначала ОБЪЯВЛЯЕТСЯ (def), а потом ВЫЗЫВАЕТСЯ.\n"
            "2. return завершает функцию и возвращает значение.\n"
            "3. Имя функции должно быть осмысленным.\n"
            "4. Внутри функции можно использовать любые конструкции."
        ),
        "tasks": [
            {
                "task": "Напишите функцию square(x), возвращающую квадрат числа, и выведите square(6).",
                "example": "def square(x):\n    return x * x\nprint(square(6))",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "1. Объявить функцию square с параметром x\n"
                    "2. Вернуть из неё x * x (квадрат)\n"
                    "3. Вызвать функцию с аргументом 6 и вывести результат\n\n"
                    "Код решения:\n"
                    "def square(x):\n"
                    "    return x * x\n"
                    "print(square(6))\n\n"
                    "Пошагово:\n"
                    "• def square(x): — объявление функции\n"
                    "• return x * x — возврат квадрата числа\n"
                    "• square(6) вызывает функцию, x = 6\n"
                    "• 6 * 6 = 36 — результат возвращается\n"
                    "• print выводит 36\n\n"
                    "Ожидаемый результат: 36"
                ),
                "expected_output": "36",
            },
            {
                "task": "Напишите функцию multiply(a, b), возвращающую произведение двух чисел, и выведите multiply(3, 4).",
                "example": "def multiply(a, b):\n    return a * b\nprint(multiply(3, 4))",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "1. Объявить функцию multiply с двумя параметрами a и b\n"
                    "2. Вернуть произведение a * b\n"
                    "3. Вызвать multiply(3, 4) и вывести результат\n\n"
                    "Код решения:\n"
                    "def multiply(a, b):\n"
                    "    return a * b\n"
                    "print(multiply(3, 4))\n\n"
                    "Пошагово:\n"
                    "• def multiply(a, b): — функция с двумя параметрами\n"
                    "• return a * b — возвращает произведение\n"
                    "• multiply(3, 4) — a = 3, b = 4\n"
                    "• 3 * 4 = 12 — результат возвращается\n\n"
                    "Ожидаемый результат: 12"
                ),
                "expected_output": "12",
            },
        ],
    },
]


class LearnPythonApp(toga.App):
    def startup(self):
        self.current_lesson_index = 0
        self.current_task_index = 0
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.build_lesson_list_screen()
        self.main_window.show()

    def build_lesson_list_screen(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=20, flex=1))

        title_label = toga.Label(
            "🐍 Уроки Python",
            style=Pack(font_size=26, font_weight="bold",
                       margin_bottom=20, text_align=CENTER),
        )
        main_box.add(title_label)

        for index, lesson in enumerate(LESSONS):
            btn = toga.Button(
                f"{index + 1}. {lesson['title']}",
                on_press=self.open_lesson,
                style=BTN_STYLE,
            )
            btn.lesson_index = index
            main_box.add(btn)

        return main_box

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

        task_label = toga.Label(
            f"📝 {task['task']}",
            style=Pack(font_size=14, font_weight="bold", margin=5),
        )
        main_box.add(task_label)

        example_label = toga.Label(
            "Пример:",
            style=Pack(font_size=13, font_weight="bold",
                       margin_left=5, margin_top=5),
        )
        main_box.add(example_label)

        example_code = toga.MultilineTextInput(
            readonly=True,
            value=task.get("example", ""),
            style=Pack(flex=1, margin=5),
        )
        main_box.add(example_code)

        self.code_editor = toga.MultilineTextInput(
            placeholder="Введите ваш код здесь...",
            style=Pack(flex=2, margin=5),
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
            self.output_text.value = "✅ Верно! Отличная работа."
        else:
            self.output_text.value = (
                f"❌ Не совсем.\n\n"
                f"Ожидалось:\n{expected}\n\n"
                f"Ваш вывод:\n{user_output if user_output else '(пусто)'}"
            )


def main():
    return LearnPythonApp()
