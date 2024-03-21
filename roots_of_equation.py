import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter as tk
from tkinter import simpledialog


ROOT = tk.Tk()
ROOT.withdraw()

# ===================================================================================================

# Коды ошибок:
# 0 - Корень успешно найден
# 1 - На заданном интервале нет корня или есть более одного корня (знак функции не меняется на концах интервала)
# 2 - Деление на ноль в процессе вычислений (знаменатель в формуле метода секущих обращается в ноль)
# 3 - Превышено максимальное количество итераций (корень не найден с заданной точностью в пределах максимального количества итераций)

# ===================================================================================================

# Ввод пользователем функции и параметров
# Запрос функции и параметров от пользователя через классные окошки
user_function = simpledialog.askstring(title="Ввод функции", prompt="Введите функцию f(x) в аналитическом виде:")
a = float(simpledialog.askstring(title="Начало отрезка", prompt="Введите начало отрезка a:"))
b = float(simpledialog.askstring(title="Конец отрезка", prompt="Введите конец отрезка b:"))
h = float(simpledialog.askstring(title="Шаг деления отрезка", prompt="Введите шаг деления отрезка h:"))
Nmax = int(simpledialog.askstring(title="Максимальное количество итераций", prompt="Введите максимальное количество итераций Nmax:"))
eps = float(simpledialog.askstring(title="Точность", prompt="Введите точность eps:"))

# ===================================================================================================

# Определение функции на основе пользовательского ввода
# Преобразование функции в символьное выражение для вычисления производных и точек экстремума и перегиба
x_sym = sp.symbols('x')
f_sym = sp.sympify(user_function)

# Первая и вторая производная функции
f_prime = sp.diff(f_sym, x_sym)
f_double_prime = sp.diff(f_prime, x_sym)

# Нахождение корней первой и второй производной
extremum_points = [sp.re(point) for point in sp.solveset(f_prime, x_sym, domain=sp.S.Reals)]
inflection_points = [sp.re(point) for point in sp.solveset(f_double_prime, x_sym, domain=sp.S.Reals)]
    
# Переводим sympy выражение в функцию, которую можно вызвать
f = sp.lambdify(x_sym, f_sym, 'numpy')

# ===================================================================================================

# Метод секущих
def secant_method(a, b, eps, Nmax):
    if f(a) * f(b) >= 0:
        return None, 0, 1  # Корней нет или их несколько
    x0 = a
    x1 = b
    for n in range(1, Nmax + 1):
        if f(x1) - f(x0) == 0:
            return None, n, 2  # Деление на ноль
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)) # формула нагло украдена у математиков!
        if abs(x2 - x1) < eps:
            return x2, n, 0  # Корень найден
        x0, x1 = x1, x2
    return x2, Nmax, 3  # Превышено максимальное количество итераций

# Поиск корней. Идем по интервалам
results = []
x = a
while x < b:
    x_next = min(x + h, b)
    root, iterations, error_code = secant_method(x, x_next, eps, Nmax)
    if root is not None:
        results.append((x, x_next, root, f(root), iterations, error_code))
    x = x_next

# ===================================================================================================

# Вывод результатов для каждого интервала
print(f"{'№':^3} {'Интервал':^20} {'Найден x?':^10} {'x':^15} {'f(x)':^20} {'Итерации':^10} {'Код ошибки':^10}")
interval_number = 1
x = a
while x < b:
    x_next = min(x + h, b)
    root, iterations, error_code = secant_method(x, x_next, eps, Nmax)
    interval_str = f"[{x:.2f}, {x_next:.2f}]"
    if root is not None:
        print(f"{interval_number:^3} {interval_str:^20} {'Да':^10} {root:^15.5f} {f(root):^20e} {iterations:^10} {error_code:^10}")
    else:
        print(f"{interval_number:^3} {interval_str:^20} {'Нет':^10} {'-':^15} {'-':^20} {'-':^10} {error_code:^10}")
    x = x_next
    interval_number += 1

# Визуализация функции
x_points = np.linspace(a, b, 1000)
y_points = f(x_points)
plt.plot(x_points, y_points, label='f(x)', color='black')  

# Отмечаем корни
for _, _, root, _, _, _ in results:
    plt.scatter(root, f(root), color='green', label='Roots' if root == results[0][2] else "")

# Отмечаем точки экстремума
for point in extremum_points:
    plt.scatter(point, f(point), color='red', label='Extremum' if point == extremum_points[0] else "")

# Отмечаем точки перегиба
for point in inflection_points:
    plt.scatter(point, f(point), color='blue', label='Inflection' if point == inflection_points[0] else "")

plt.axhline(0, color='grey', lw=0.5)  # Ось X

# Настройка легенды
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.show()
