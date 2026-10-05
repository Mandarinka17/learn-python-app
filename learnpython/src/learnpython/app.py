"""
Приложение для изучения основ Python
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
import sys
import io


# --- Данные уроков ---
LESSONS = [
    {
        "title": "Урок 1: Переменные",
        "theory": (
            "Переменная — это контейнер для хранения данных.\n\n"
            "Пример:\n"
            "name = 'Анна'\n"
            "age = 25\n"
            "print(name)"
        ),
        "task": "Создайте переменную x = 5 и выведите её на экран.",
        "expected_output": "5",
    },
    {
        "title": "Урок 2: Цикл for",
        "theory": (
            "Цикл for повторяет действия несколько раз.\n\n"
            "Пример:\n"
            "for i in range(3):\n"
            "    print(i)"
        ),
        "task": "Выведите числа от 0 до 2 с помощью цикла for.",
        "expected_output": "0\n1\n2",
    },
    {
        "title": "Урок 3: Функции",
        "theory": (
            "Функция — это блок кода, который можно вызывать многократно.\n\n"
            "Пример:\n"
            "def greet(name):\n"
            "    return f'Привет, {name}!'\n"
            "print(greet('Мир'))"
        ),
        "task": "Напишите функцию square(x), возвращающую квадрат числа, и выведите square(4).",
        "expected_output": "16",
    },
]


class LearnPythonApp(toga.App):
    def startup(self):
        """Инициализация главного окна."""
        self.current_lesson_index = 0

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.build_lesson_list_screen()
        self.main_window.show()

    # --- Экран 1: Список уроков ---
    def build_lesson_list_screen(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, margin=20))

        title_label = toga.Label(
            "📚 Уроки Python",
            style=Pack(font_size=24, font_weight="bold", margin_bottom=20, text_align=CENTER),
        )
        main_box.add(title_label)

        for index, lesson in enumerate(LESSONS):
            btn = toga.Button(
                f"{index + 1}. {lesson['title']}",
                on_press=self.open_lesson,
                style=Pack(margin=5),
            )
            btn.lesson_index = index
            main_box.add(btn)

        return main_box

    # --- Экран 2: Теория и задание ---
    def open_lesson(self, widget):
        self.current_lesson_index = widget.lesson_index
        lesson = LESSONS[self.current_lesson_index]

        content = toga.Box(style=Pack(direction=COLUMN, margin=15))
        scroll = toga.ScrollContainer(content=content, style=Pack(flex=1))

        back_btn = toga.Button(
            "← Назад",
            on_press=self.go_back_to_list,
            style=Pack(margin_bottom=10),
        )
        content.add(back_btn)

        title = toga.Label(
            lesson["title"],
            style=Pack(font_size=20, font_weight="bold", margin_bottom=10),
        )
        content.add(title)

        theory = toga.Label(lesson["theory"], style=Pack(margin_bottom=20))
        content.add(theory)

        task = toga.Label(
            f"📝 Задание: {lesson['task']}",
            style=Pack(font_size=14, margin_bottom=10),
        )
        content.add(task)

        practice_btn = toga.Button(
            "✏️ Перейти к практике",
            on_press=self.open_practice_screen,
            style=Pack(margin_top=10),
        )
        content.add(practice_btn)

        self.main_window.content = scroll

    def go_back_to_list(self, widget):
        self.main_window.content = self.build_lesson_list_screen()

    # --- Экран 3: Практика ---
    def open_practice_screen(self, widget):
        lesson = LESSONS[self.current_lesson_index]

        main_box = toga.Box(style=Pack(direction=COLUMN, margin=15, flex=1))

        back_btn = toga.Button(
            "← Назад к теории",
            on_press=self.go_back_to_theory,
            style=Pack(margin_bottom=10),
        )
        main_box.add(back_btn)

        task_label = toga.Label(
            f"Задание: {lesson['task']}",
            style=Pack(margin_bottom=10),
        )
        main_box.add(task_label)

        self.code_editor = toga.MultilineTextInput(
            placeholder="Введите ваш код здесь...",
            style=Pack(flex=2, margin_bottom=10),
        )
        main_box.add(self.code_editor)

        btn_row = toga.Box(style=Pack(direction=ROW, margin_bottom=10))
        run_btn = toga.Button("▶ Запустить", on_press=self.run_code, style=Pack(flex=1, margin_right=5))
        check_btn = toga.Button("✅ Проверить", on_press=self.check_answer, style=Pack(flex=1, margin_left=5))
        btn_row.add(run_btn)
        btn_row.add(check_btn)
        main_box.add(btn_row)

        self.output_text = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=1),
        )
        main_box.add(self.output_text)

        self.main_window.content = main_box

    def go_back_to_theory(self, widget):
        lesson = LESSONS[self.current_lesson_index]
        # Создаем "фиктивный" виджет с индексом урока
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

    def check_answer(self, widget):
        code = self.code_editor.value
        user_output = self.execute_code(code)
        expected = LESSONS[self.current_lesson_index]["expected_output"].strip()

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