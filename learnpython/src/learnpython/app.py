"""
Приложение для изучения основ Python
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
import sys
import io


# --- Данные уроков с задачами и разборами ---
LESSONS = [
    {
        "title": "Урок 1: Переменные",
        "theory": (
            "ПЕРЕМЕННАЯ — это именованный контейнер для хранения данных. "
            "Когда вы пишете «x = 5», вы создаёте переменную x, которая "
            "хранит число 5.\n\n"

            "📌 ПРАВИЛА ИМЕНОВАНИЯ:\n"
            "• Имя может содержать буквы, цифры и знак _\n"
            "• Имя не может начинаться с цифры\n"
            "• Регистр важен: name и Name — разные переменные\n\n"

            "📌 ТИПЫ ДАННЫХ:\n"
            "• int — целые числа: 5, -10, 100\n"
            "• float — дробные: 3.14, 2.5\n"
            "• str — строки: 'Анна', \"Привет\"\n"
            "• bool — логические: True, False\n\n"

            "📌 ПРИМЕР 1 — Числа и строки:\n"
            "name = 'Анна'\n"
            "age = 25\n"
            "print(name)\n"
            "print(age)\n"
            "Результат: Анна, затем 25\n\n"

            "📌 ПРИМЕР 2 — Операции с переменными:\n"
            "x = 10\n"
            "y = 3\n"
            "print(x + y)\n"
            "print(x * y)\n"
            "Результат: 13, затем 30"
        ),
        "tasks": [
            {
                "task": "Создайте переменную x = 5 и выведите её на экран.",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "1. Создать переменную с именем x\n"
                    "2. Положить в неё число 5\n"
                    "3. Вывести значение на экран\n\n"
                    "Код решения:\n"
                    "x = 5\n"
                    "print(x)\n\n"
                    "Пошагово:\n"
                    "• x = 5 — создаём переменную и кладём в неё 5\n"
                    "• print(x) — выводим то, что хранится в x\n\n"
                    "Ожидаемый результат: 5"
                ),
                "expected_output": "5",
            },
            {
                "task": "Создайте две переменные: name = 'Анна' и age = 25. Выведите их на экран (каждое с новой строки).",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "1. Создать переменную name со значением 'Анна'\n"
                    "2. Создать переменную age со значением 25\n"
                    "3. Вывести обе переменные — каждую на своей строке\n\n"
                    "Код решения:\n"
                    "name = 'Анна'\n"
                    "age = 25\n"
                    "print(name)\n"
                    "print(age)\n\n"
                    "Пошагово:\n"
                    "• name = 'Анна' — строковая переменная\n"
                    "• age = 25 — числовая переменная\n"
                    "• Два print() выводят каждую на своей строке\n\n"
                    "Ожидаемый результат:\nАнна\n25"
                ),
                "expected_output": "Анна\n25",
            },
        ],
    },
    {
        "title": "Урок 2: Цикл for",
        "theory": (
            "ЦИКЛ — это конструкция, которая повторяет блок кода "
            "несколько раз. Цикл for используется, когда известно "
            "количество повторений.\n\n"

            "📌 СИНТАКСИС:\n"
            "for переменная in последовательность:\n"
            "    код_который_повторяется\n\n"

            "📌 ФУНКЦИЯ range():\n"
            "• range(3) — числа 0, 1, 2\n"
            "• range(1, 4) — числа 1, 2, 3\n"
            "• range(0, 10, 2) — 0, 2, 4, 6, 8\n\n"

            "📌 ПРИМЕР 1 — Простой цикл:\n"
            "for i in range(3):\n"
            "    print(i)\n"
            "Результат: 0, затем 1, затем 2\n\n"

            "📌 ПРИМЕР 2 — Цикл по строке:\n"
            "word = 'Python'\n"
            "for letter in word:\n"
            "    print(letter)\n"
            "Результат: каждая буква на новой строке"
        ),
        "tasks": [
            {
                "task": "Выведите числа от 0 до 2 с помощью цикла for.",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "Вывести три числа: 0, 1, 2 — каждое на своей строке.\n\n"
                    "Код решения:\n"
                    "for i in range(3):\n"
                    "    print(i)\n\n"
                    "Пошагово:\n"
                    "• range(3) создаёт последовательность 0, 1, 2\n"
                    "• Переменная i принимает по очереди каждое значение\n"
                    "• print(i) выводит текущее значение\n\n"
                    "ВАЖНО: отступ перед print() — 4 пробела!\n\n"
                    "Ожидаемый результат:\n0\n1\n2"
                ),
                "expected_output": "0\n1\n2",
            },
            {
                "task": "Выведите числа от 1 до 3 с помощью цикла for.",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "Вывести три числа: 1, 2, 3 — каждое на своей строке.\n\n"
                    "Код решения:\n"
                    "for i in range(1, 4):\n"
                    "    print(i)\n\n"
                    "Пошагово:\n"
                    "• range(1, 4) — от 1 включительно до 4 НЕ включительно\n"
                    "• То есть числа: 1, 2, 3\n"
                    "• Цикл выводит каждое из них\n\n"
                    "ВАЖНО: правая граница не входит!\n"
                    "range(1, 4) — это 1, 2, 3, а не 1, 2, 3, 4.\n\n"
                    "Ожидаемый результат:\n1\n2\n3"
                ),
                "expected_output": "1\n2\n3",
            },
        ],
    },
    {
        "title": "Урок 3: Функции",
        "theory": (
            "ФУНКЦИЯ — это блок кода, который можно вызывать "
            "многократно по имени. Функции делают программу "
            "короче и понятнее.\n\n"

            "📌 СИНТАКСИС:\n"
            "def имя_функции(параметры):\n"
            "    тело_функции\n"
            "    return результат\n\n"

            "📌 КЛЮЧЕВОЕ СЛОВО return:\n"
            "Возвращает значение из функции. Без return "
            "функция возвращает None.\n\n"

            "📌 ПРИМЕР 1 — Функция с возвратом:\n"
            "def square(x):\n"
            "    return x * x\n"
            "print(square(4))\n"
            "Результат: 16\n\n"

            "📌 ПРИМЕР 2 — Функция с двумя параметрами:\n"
            "def greet(name, age):\n"
            "    return f'Привет, {name}! Тебе {age} лет.'\n"
            "print(greet('Анна', 25))\n"
            "Результат: Привет, Анна! Тебе 25 лет."
        ),
        "tasks": [
            {
                "task": "Напишите функцию square(x), возвращающую квадрат числа, и выведите square(4).",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "1. Объявить функцию square с параметром x\n"
                    "2. Вернуть из неё x * x (квадрат)\n"
                    "3. Вызвать функцию с аргументом 4 и вывести результат\n\n"
                    "Код решения:\n"
                    "def square(x):\n"
                    "    return x * x\n"
                    "print(square(4))\n\n"
                    "Пошагово:\n"
                    "• def square(x): — объявление функции\n"
                    "• return x * x — возврат квадрата числа\n"
                    "• square(4) вызывает функцию, x = 4\n"
                    "• 4 * 4 = 16 — результат возвращается\n"
                    "• print выводит 16 на экран\n\n"
                    "Ожидаемый результат: 16"
                ),
                "expected_output": "16",
            },
            {
                "task": "Напишите функцию add(a, b), возвращающую сумму двух чисел, и выведите add(3, 7).",
                "explanation": (
                    "📖 РАЗБОР:\n\n"
                    "Что нужно сделать:\n"
                    "1. Объявить функцию add с двумя параметрами a и b\n"
                    "2. Вернуть сумму a + b\n"
                    "3. Вызвать add(3, 7) и вывести результат\n\n"
                    "Код решения:\n"
                    "def add(a, b):\n"
                    "    return a + b\n"
                    "print(add(3, 7))\n\n"
                    "Пошагово:\n"
                    "• def add(a, b): — функция с двумя параметрами\n"
                    "• return a + b — возвращает сумму\n"
                    "• add(3, 7) — a = 3, b = 7\n"
                    "• 3 + 7 = 10 — результат возвращается\n"
                    "• print выводит 10\n\n"
                    "Ожидаемый результат: 10"
                ),
                "expected_output": "10",
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

    # --- Экран 1: Список уроков ---
    def build_lesson_list_screen(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=20, flex=1))

        title_label = toga.Label(
            "📚 Уроки Python",
            style=Pack(
                font_size=24, font_weight="bold", margin_bottom=20,
                text_align=CENTER, flex=1,
            ),
        )
        main_box.add(title_label)

        for index, lesson in enumerate(LESSONS):
            count = len(lesson["tasks"])
            btn = toga.Button(
                f"{index + 1}. {lesson['title']} ({count} задачи)",
                on_press=self.open_lesson,
                style=Pack(margin=5, flex=1),
            )
            btn.lesson_index = index
            main_box.add(btn)

        return main_box

    # --- Экран 2: Теория и разборы задач ---
    def open_lesson(self, widget):
        self.current_lesson_index = widget.lesson_index
        lesson = LESSONS[self.current_lesson_index]

        content = toga.Box(style=Pack(direction=COLUMN, margin=15, flex=1))
        scroll = toga.ScrollContainer(
            content=content, style=Pack(flex=1),
            horizontal=False,
        )

        back_btn = toga.Button(
            "← Назад к списку",
            on_press=self.go_back_to_list,
            style=Pack(margin_bottom=10, flex=1),
        )
        content.add(back_btn)

        title = toga.Label(
            lesson["title"],
            style=Pack(font_size=20, font_weight="bold", margin_bottom=10, flex=1),
        )
        content.add(title)

        theory = toga.Label(
            lesson["theory"],
            style=Pack(margin_bottom=20, flex=1),
        )
        content.add(theory)

        # Раздел "Задачи к уроку"
        tasks_header = toga.Label(
            "\n📝 ЗАДАЧИ К УРОКУ:",
            style=Pack(font_size=18, font_weight="bold", margin_bottom=10, flex=1),
        )
        content.add(tasks_header)

        for idx, task in enumerate(lesson["tasks"], start=1):
            task_title = toga.Label(
                f"\nЗАДАЧА {idx}: {task['task']}",
                style=Pack(font_size=15, font_weight="bold", margin_top=10, flex=1),
            )
            content.add(task_title)

            explanation = toga.Label(
                task["explanation"],
                style=Pack(font_size=13, margin_bottom=15, flex=1),
            )
            content.add(explanation)

        practice_btn = toga.Button(
            "✏️ Перейти к практике",
            on_press=self.open_practice_screen,
            style=Pack(margin_top=20, margin_bottom=20, flex=1),
        )
        content.add(practice_btn)

        self.main_window.content = scroll

    def go_back_to_list(self, widget):
        self.main_window.content = self.build_lesson_list_screen()

    # --- Экран 3: Практика с переключением задач ---
    def open_practice_screen(self, widget):
        self.current_task_index = 0
        self.render_practice_screen()

    def render_practice_screen(self):
        lesson = LESSONS[self.current_lesson_index]
        task = lesson["tasks"][self.current_task_index]

        main_box = toga.Box(style=Pack(direction=COLUMN, margin=15, flex=1))

        # Верхняя кнопка "Назад"
        back_btn = toga.Button(
            "← Назад к теории",
            on_press=self.go_back_to_theory,
            style=Pack(margin_bottom=10, flex=1),
        )
        main_box.add(back_btn)

        # Переключатель задач
        if len(lesson["tasks"]) > 1:
            switch_row = toga.Box(style=Pack(direction=ROW, margin_bottom=10, flex=1))
            for idx, t in enumerate(lesson["tasks"]):
                label = f"Задача {idx + 1}"
                if idx == self.current_task_index:
                    label = f"▶ {label}"
                btn = toga.Button(
                    label,
                    on_press=self.switch_task,
                    style=Pack(flex=1, margin_left=2, margin_right=2),
                )
                btn.task_index = idx
                switch_row.add(btn)
            main_box.add(switch_row)

        # Текущее задание
        task_label = toga.Label(
            f"📝 {task['task']}",
            style=Pack(font_size=14, font_weight="bold", margin_bottom=10, flex=1),
        )
        main_box.add(task_label)

        # Кнопка "Показать разбор"
        explain_btn = toga.Button(
            "💡 Показать разбор",
            on_press=self.show_explanation,
            style=Pack(margin_bottom=10, flex=1),
        )
        main_box.add(explain_btn)

        # Редактор кода
        self.code_editor = toga.MultilineTextInput(
            placeholder="Введите ваш код здесь...",
            style=Pack(flex=2, margin_bottom=10),
        )
        main_box.add(self.code_editor)

        # Кнопки Запустить / Проверить
        btn_row = toga.Box(style=Pack(direction=ROW, margin_bottom=10, flex=1))
        run_btn = toga.Button(
            "▶ Запустить",
            on_press=self.run_code,
            style=Pack(flex=1, margin_right=5),
        )
        check_btn = toga.Button(
            "✅ Проверить",
            on_press=self.check_answer,
            style=Pack(flex=1, margin_left=5),
        )
        btn_row.add(run_btn)
        btn_row.add(check_btn)
        main_box.add(btn_row)

        # Поле вывода
        self.output_text = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=2),
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

    # --- Логика выполнения кода ---
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