import tkinter as tk
from tkinter import filedialog
import random
import os


def load_file():
    global last_opened_file
    global all_ind, A_I
    filepath = filedialog.askopenfilename(initialdir=os.path.dirname(last_opened_file))
    if filepath:
        last_opened_file = filepath
        text.clear()
        with open(filepath, 'r', encoding='utf-8') as file:
            text.extend(file.readlines())
        generate_button.config(state=tk.NORMAL)
    all_ind = [i for i in range(0, len(text))]
    A_I =  all_ind
    

def generate_question():
    global ind, all_ind
    ind = random.choice(all_ind)

    all_ind.pop(ind)
    question_label.config(text=text[ind])

def clear_questions():
    global all_ind
    all_ind = A_I
    question_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Вопросник")

text = []

ind = -1
last_opened_file = os.getcwd()  # Изначально текущий каталог

# Widgets
load_button = tk.Button(root, text="Выбрать файл", command=load_file, font=("Arial", 12), padx=10, pady=5)
generate_button = tk.Button(root, text="Сгенерировать вопрос", state=tk.DISABLED, command=generate_question, font=("Arial", 12), padx=10, pady=5)
clear_button = tk.Button(root, text="Очистить историю вопросов", command=clear_questions, font=("Arial", 12), padx=10, pady=5)
question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12))

# Layout
load_button.pack(pady=10)
generate_button.pack(pady=10)
clear_button.pack(pady=10)
question_label.pack(pady=10)

# Run the application
root.mainloop()
