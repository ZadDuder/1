import tkinter as tk
from tkinter import messagebox

#from converter import tri_to_dec, dec_to_tri

class TriSymmetricCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Троично-симметричный калькулятор")
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=0, columnspan=6, sticky="nsew")
        self.result_label = tk.Label(self, text="Результат: ")
        self.result_label.grid(row=1, column=0, columnspan=6, sticky="nsew")

        # Кнопки для ввода цифр десятичной системы
        button_texts = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            'Z', '0', 'Convert to Dec',
            'Convert to Tri', 'Clear', 'Back', 'Info'
        ]

        row = 2
        col = 0
        for text in button_texts:
            if text in ['2', '5', '8', '0', 'Clear']:
                btn = tk.Button(self, text=text, command=lambda b=text: self.on_button_click(b), width=10)
            else:
                btn = tk.Button(self, text=text, command=lambda b=text: self.on_button_click(b))
            btn.grid(row=row + (col // 3), column=col % 3, sticky="nsew", padx=5, pady=5)
            col += 1

        # Распределение пространства
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Convert to Dec", command=self.convert_to_dec)
        file_menu.add_command(label="Convert to Tri", command=self.convert_to_tri)
        file_menu.add_command(label="Clear Entry", command=lambda: self.entry.delete(0, tk.END))
        file_menu.add_command(label="Clear Result", command=lambda: self.result_label.config(text="Результат: "))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: messagebox.showinfo("Информация", "Автор: Тымчишин ИУ7-21Б\nПрограмма для перевода чисел между троично-симметричной и десятичной системами счисления."))

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

    def on_button_click(self, button):
        if button in [str(digit) for digit in range(10)] + ['Z']:
            self.entry.insert(tk.END, button)
        elif button == 'Convert to Dec':
            self.convert_to_dec()
        elif button == 'Convert to Tri':
            self.convert_to_tri()
        elif button == 'Clear':
            self.entry.delete(0, tk.END)
            self.result_label.config(text="Результат: ")
        elif button == 'Back':
            entry_text = self.entry.get()
            self.entry.delete(len(entry_text)-1, tk.END)
        elif button == 'Info':
            messagebox.showinfo("Информация", "Автор: Тымчишин ИУ7-21Б\nПрограмма для перевода чисел между троично-симметричной и десятичной системами счисления.")

    def tri_to_dec(self, tri_str):
        """Переводит число из троично-симметричной системы в десятичную."""
        decimal = 0
        for i, digit in enumerate(reversed(tri_str)):
            if digit == 'Z':
                decimal += -1 * (3 ** i)
            else:
                decimal += int(digit) * (3 ** i)
        return decimal

    def dec_to_tri(self, decimal):
        """Переводит число из десятичной системы в троично-симметричную."""
        if decimal == 0:
            return '0'
        digits = []
        abs_decimal = abs(decimal)
        while abs_decimal > 0:
            remainder = abs_decimal % 3
            abs_decimal //= 3
            if remainder == 2:
                digits.append('Z')
                abs_decimal += 1
            elif remainder == 1:
                digits.append('1')
            else:
                digits.append('0')
        if decimal < 0:
            return '-' + ''.join(reversed(digits))
        return ''.join(reversed(digits))

    def convert_to_dec(self):
        tri_str = self.entry.get()
        if not tri_str or not all(c in '10Z' for c in tri_str):
            messagebox.showerror("Ошибка", "Введите корректное число в троично-симметричной системе (только 1, 0, Z).")
        else:
            result = self.tri_to_dec(tri_str)
            self.result_label.config(text=f"Результат: {result}")

    def convert_to_tri(self):
        dec_str = self.entry.get()
        try:
            dec_value = int(dec_str)
            result = self.dec_to_tri(dec_value)
            self.result_label.config(text=f"Результат: {result}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное десятичное число.")

if __name__ == "__main__":
    app = TriSymmetricCalculator()
    app.mainloop()
