#Графики . Тымчишин Егор ИУ7-11Б
import math
EPS = 1e-9
a = float(input("Введите начальное значение аргумента: "))
b = float(input("Введите конечное значение аргумента: "))
h = float(input("Введите шаг: "))
#шапка таблицы
print ("-" * 49)
print ("|" + " " * 7 + "x" + " " * 7 + "|" + " " * 7 + "y1" + " " * 6 + "|" + " " * 7 + "y2" + " " * 6 + "|")
print ("|" + "-" * 47 + "|")
#таблица со значениями
for x in range (int(round(a, 7)*10**7), int(round(b, 7)*10**7 ) + int (round(h, 7)*10**7), int (round(h, 7)*10**7)):
    x = x/10000000
    y1 = math.exp(-x) + x**2 - 2
    y2 = x**3 - 19.7 * x**2 + 28.9 * x + 5.62
    print ("|{:^15.5g}|{:^15.5g}|{:^15.5g}|".format(x, y1, y2))
print ("-" * 49)
values_num = int((b - a + EPS) / h) + 1 #
x = a
minf1_v = maxf1_v = math.exp(-x) + x**2 - 2
for _ in range(values_num):
    y1 = math.exp(-x) + x**2 - 2
    maxf1_v = max(y1, maxf1_v)
    minf1_v = min(y1, minf1_v)
    x += h

room = 8    # под засечку выделяем 8 символов
graph_wd = 100   # ширина графика
scale = (maxf1_v - minf1_v) / graph_wd # ширина одного знакоместа
notch = int(input("Введите количество засечек (от 4 до 8): "))
notch += 1
notch_step = (maxf1_v - minf1_v) / (notch - 1) # шаг засечек
notches_values = [minf1_v + i * notch_step for i in range(notch)] # значения засечек
notches_positions = [int((nv - minf1_v) / scale) for nv in notches_values] #позиция засечек
# Вывод строки с засечками
print(" " * room, end='')  # отступ под значения x
l=0
for k in range(graph_wd):
    if k in notches_positions:
        print("{:.6g}".format(notches_values[l]), end='')   # Засечка
        l += 1
    else:
        print(" ", end='')  # Пустое место
print()  # Переход на новую строку после засечек

x = a
for _ in range(values_num):
    print(f"{x:^{room}.6g}|", end='') #выводим слева значения х
    y1 = math.exp(-x) + x**2 - 2
    # Рисуем строку графика для каждой абсциссы
    line = ''
    for k in range(graph_wd):
        if (scale*k <= y1 - minf1_v < scale*(k + 1)):
            line += "*"
        elif (-EPS <= scale*k + minf1_v < EPS):
            line += "|"
        else:
            line += " "
    print(line)
    x += h
print ()
# ЗАЩИТА
print ("ПРОИЗВОДНАЯ!!!!!!")
print ()
# Для производной
minf1_der_v = float('inf')
maxf1_der_v = float('-inf')
derivatives = []

x = a
for _ in range(values_num - 1):  
    y1_current = math.exp(-x) + x**2 - 2
    y1_next = math.exp(-(x+h)) + (x+h)**2 - 2
    y1_prime = (y1_next - y1_current) / h
    derivatives.append(y1_prime)
    maxf1_der_v = max(y1_prime, maxf1_der_v)
    minf1_der_v = min(y1_prime, minf1_der_v)
    x += h

scale_der = (maxf1_der_v - minf1_der_v) / graph_wd

x = a
for y1_prime in derivatives:
    print(f"{x:^{room}.6g}|", end='') 
    line = ''
    for k in range(graph_wd):
        if (scale_der*k <= y1_prime - minf1_der_v < scale_der*(k + 1)):
            line += "*"
        elif (-EPS <= scale_der*k + minf1_der_v < EPS):
            line += "|"
        else:
            line += " "
    print(line)
    x += h
