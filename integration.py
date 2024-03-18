#Тымчишин. ИУ7-11Б
import math
# Задаем функцию для интегрирования и ее первообразную
my_function = lambda x: math.sin(x)  # Ваша интегрируемая функция
my_primitive = lambda x: -math.cos(x)  # Первообразная от функции

# Функция для безопасного ввода списка значений определенного типа
def safe_multiple_input(msg: str, data_type, count: int, sep: str = " ") -> list:
    while True:
        values = []
        user_input = input(msg).split(sep)
        all_valid = True
        if len(user_input) != count:
            print(f"Необходимо ввести {count} элементов, но введено {len(user_input)}")
            continue
        for item in user_input:
            try:
                converted = data_type(item)
                values.append(converted)
            except Exception as e:
                all_valid = False
                print(f"Исключение {e} при обработке значения ({item!r})")
                break
        if all_valid:
            return values

# Функция для безопасного ввода числа заданного типа
def safe_num_input(msg: str, data_type):
    while True:
        user_input = input(msg)
        try:
            return data_type(user_input)
        except ValueError:
            print(f"Неверное значение ({user_input!r})")

# Функция для вычисления интеграла методом срединных прямоугольников
def integrate_rectangles(f, start, stop, N):
    result = 0
    step = (stop - start) / N
    for i in range(N):
        # Вычисляем значение функции в середине текущего интервала и умножаем на ширину интервала
        result += f((i * step + (i + 1) * step) / 2 + start) * step
    return result

# Функция для вычисления интеграла методом парабол
def integrate_parabolas(f, start: float, stop: float, N: int) -> float:
    N = math.ceil(N / 2) * 2  # Приводим N к четному числу
    step = (stop - start) / N
    result = 0
    for i in range(0, N, 2):
        # Используем формулу парабол для интервала и умножаем на ширину интервала (формула Симпсона)
        result += (step / 3) * (
                f(step * i + start)
                + 4 * f(step * (i + 1) + start)
                + f(step * (i + 2) + start)
        )
    return result

# Функция для вычисления значения интеграла с заданной точностью
def calculate_with_precision(f, precision: float, max_attempts: int = None) -> tuple[int, float]:
    N = 2
    integral = f(N)  # Начальное значение интеграла
    integral_2 = f(N * 2)  # Значение интеграла при удвоенном количестве интервалов
    N *= 2
    i = 0
    while abs(integral - integral_2) > precision or (max_attempts and i <= max_attempts):
        i += 1
        integral = integral_2
        integral_2 = f(N * 2)  # Удваиваем количество интервалов и вычисляем новое значение интеграла
        N *= 2
    return N, integral_2

# Функция для вычисления абсолютной ошибки
def absolute_error(res1: float, res2: float) -> float:
    return abs(res2 - res1)

# Функция для вычисления относительной ошибки
def relative_error(res1: float, res2: float) -> float:
    return abs(absolute_error(res1, res2) / res2)

# Основная функция программы
def main() -> None:
    N1 = safe_num_input(">>> Введите количество участков разбиения N1: ", int)
    N2 = safe_num_input(">>> Введите количество участков разбиения N2: ", int)
    a, b = safe_multiple_input(">>> Введите начало и конец отрезка интегрирования через пробел: ", float, 2)

    i1 = integrate_rectangles(my_function, a, b, N1)  # Вычисление интеграла методом срединных прямоугольников
    i2 = integrate_rectangles(my_function, a, b, N2)  # Вычисление интеграла методом срединных прямоугольников
    i3 = integrate_parabolas(my_function, a, b, N1)  # Вычисление интеграла методом парабол
    i4 = integrate_parabolas(my_function, a, b, N2)  # Вычисление интеграла методом парабол
    prim_diff = my_primitive(b) - my_primitive(a)  # Разность первообразных в конечной и начальной точках

    print(" " + "_" * 47)
    print(f"|{'':^15}|{'N1':^15}|{'N2':^15}|")
    print(" " + "-" * 47)
    print(f"|{'Method 1':<15}|{i1:^15.6g}|{i2:^15.6g}|")
    print(f"|{'Method 2':<15}|{i3:^15.6g}|{i4:^15.6g}|")
    print(" " + "-" * 47)
    min_precision = safe_num_input(">>> Введите необходимую точность: ", float)

    less_accurate = None
    if abs(prim_diff - i2) > abs(prim_diff - i4):
        less_accurate = lambda x: integrate_rectangles(my_function, a, b, x)
        print("Метод срединных прямоугольников менее точен по сравнению с методом парабол")
    else:
        less_accurate = lambda x: integrate_parabolas(my_function, a, b, x)
        print("Метод парабол менее точен по сравнению с методом срединных прямоугольников")

    print(" ")
    print(" " + "_" * 47)
    print(f"|{'Method':^15}|{'Rectangles':^15}|{'Parabolas':^15}|")
    print(" " + "-" * 47)
    print(f"|{'Abs. error':<15}|{absolute_error(i1, i2):^15.6g}|{absolute_error(i3, i4):^15.6g}|")
    print(f"|{'Rel. error':<15}|{relative_error(i1, i2):^15.6g}|{relative_error(i3, i4):^15.6g}|")
    print(" " + "-" * 47)

    min_n, int_with_precision = calculate_with_precision(less_accurate, min_precision)
    print(f"Вычисленное значение интеграла с точностью {min_precision}: {int_with_precision:.6g}")
    print(f"Для вычисления интеграла с заданной точностью требуется {min_n} участков разбиения")


main()
