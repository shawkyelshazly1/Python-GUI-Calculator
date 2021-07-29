import tkinter as tk
from calc import Calculator_app


class Application(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        super().__init__(self.root)
        self.init_window()
        self.calc_app = self.start_calc()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button_2 = self.create_button(
            '2', self.outer_left_frame, lambda: self.press_digit('2')).pack()
        # self.button_sum = self.create_button(
        #     '+', lambda: self.select_operator('+'))
        # self.button_result = self.create_button(
        #     '=', lambda: self.calc_app.computation())

    def create_button(self, text, frame, command=None):
        return self.Button(
            self, {'text': text, 'command': command, })

    def start_calc(self):
        calc_app = Calculator_app()
        return calc_app

    def press_digit(self, digit):
        self.calc_app.typing(digit)

    def select_operator(self, operator):
        self.calc_app.select_math_operator(operator)

    def do_math(self):
        self.calc_app.computation()

    def init_window(self):
        self.root.title('Py Calculator')
        self.root.geometry('250x250')
        self.screen_frame = tk.Frame(self.root, bg='red').pack(side='top')
        self.outer_left_frame = tk.Frame(
            self.root, bg='black').pack(side='left')
        self.inner_left_frame = tk.Frame(
            self.root, bg='blue').pack(side='left')


app = Application()
app.mainloop()
