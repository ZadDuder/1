# Тымчишин Егор Сергеевич ИУ7-11Б
import math

Ax = int(input("Введите координату первой вершины треугольника по о.X: "))
Ay = int(input("Введите координату первой вершины треугольника по о.Y: "))
Bx = int(input("Введите координату второй вершины треугольника по о.X: "))
By = int(input("Введите координату второй вершины треугольника по о.Y: "))
Cx = int(input("Введите координату третьей вершины треугольника по о.X: "))
Cy = int(input("Введите координату третьей вершины треугольника по о.Y: "))
# проверяем совпадение точек
if (Ax == Bx) and (Ay == By):
    print("Введенные данные некорректны")
    exit(0)
if (Bx == Cx) and (By == Cy):
    print("Введенные данные некорректны")
    exit(0)
if (Ax == Cx) and (Ay == Cy):
    print("Введенные данные некорректны")
    exit(0)
# считаем векторы сторон
AB_vektor_x = Bx - Ax
AB_vektor_y = By - Ay
BC_vektor_x = Cx - Bx
BC_vektor_y = Cy - By
CA_vektor_x = Ax - Cx
CA_vektor_y = Ay - Cy
# считаем длины сторон
AB = math.sqrt(pow(AB_vektor_x, 2) + pow(AB_vektor_y, 2))
BC = math.sqrt(pow(BC_vektor_x, 2) + pow(BC_vektor_y, 2))
CA = math.sqrt(pow(CA_vektor_x, 2) + pow(CA_vektor_y, 2))
# проверяем треугольник на вырожденность
if (AB + CA <= BC) or (AB + BC <= CA) or (BC + CA <= AB):
    print("Введенные данные некорректны")
    exit(0)
# находим косинусы всех углов, чтобы найти минимальный
cos_angel_AB_AC = abs(AB_vektor_x * (-CA_vektor_x) + AB_vektor_y * (-CA_vektor_y)) / math.sqrt(
    pow(AB_vektor_x, 2) + pow(AB_vektor_y, 2)) / math.sqrt(pow(CA_vektor_x, 2) + pow(CA_vektor_y, 2))
cos_angel_AB_BC = abs(BC_vektor_x * (-AB_vektor_x) + BC_vektor_y * (-AB_vektor_y)) / math.sqrt(
    pow(AB_vektor_x, 2) + pow(AB_vektor_y, 2)) / math.sqrt(pow(BC_vektor_x, 2) + pow(BC_vektor_y, 2))
cos_angel_BC_CA = abs(CA_vektor_x * (-BC_vektor_x) + CA_vektor_y * (-BC_vektor_y)) / math.sqrt(
    pow(BC_vektor_x, 2) + pow(BC_vektor_y, 2)) / math.sqrt(pow(CA_vektor_x, 2) + pow(CA_vektor_y, 2))
# ищим самый близкий косинус к единице -> найдем самый маленький угол
cos_min_angel = cos_angel_AB_AC
if (abs(1 - cos_angel_AB_BC) < abs(1 - cos_min_angel)):  cos_min_angel = cos_angel_AB_BC
if (abs(1 - cos_angel_BC_CA) < abs(1 - cos_min_angel)):  cos_min_angel = cos_angel_BC_CA
# считаем два синуса, чтобы найти высоту
sin_angel_AB_AC = float(math.sqrt(1 - pow(cos_angel_AB_AC, 2)))
sin_angel_AB_BC = float(math.sqrt(1 - pow(cos_angel_AB_BC, 2)))
# находим высоту в зависимости от того, какой угол минимальный
if (cos_angel_AB_AC == cos_min_angel):
    H = AB * sin_angel_AB_BC
if (cos_angel_AB_BC == cos_min_angel):
    H = AB * sin_angel_AB_AC
if (cos_angel_BC_CA == cos_min_angel):
    H = CA * sin_angel_AB_AC
# проверяем на прямоугольность, кос = 0 -> угол = 90
if (cos_angel_AB_AC == 0) or (cos_angel_AB_BC == 0) or (cos_angel_BC_CA == 0):
    print("Треугольник является прямоугольным")
else:
    print("Треугольник не является прямоугольным")
print("Первая сторона треугольника =", f"{AB:.6}")
print("Вторая сторона треугольника =", f"{BC:.6}")
print("Третья сторона треугольника =", f"{CA:.6}")
print("Искомая высота треугольника =", f"{H:.6}")
# запрашиваем координаты точки, чтобы проверить лежит ли она в треугольнике
Px = int(input("Введите координату первой дополнительной точки по о.X: "))
Py = int(input("Введите координату первой дополнительной точки по о.Y: "))
# находим векторные произведения векторов сторон и векторов (т.P; вершина треугольника)
mp_AB_AP = AB_vektor_x * (Py - Ay) - AB_vektor_y * (Px - Ax)
mp_BC_BP = BC_vektor_x * (Py - By) - BC_vektor_y * (Px - Bx)
mp_CA_CP = CA_vektor_x * (Py - Cy) - CA_vektor_y * (Px - Cx)
# по свойству коммунитативности векторного произвдения -> если все найденные векторные произведения имеют одинаковый знак 
# (плюс или минус), то т.P внутри треугольника
if (mp_AB_AP >= 0) and (mp_BC_BP >= 0) and (mp_CA_CP >= 0) or (mp_AB_AP <= 0) and (mp_BC_BP <= 0) and (mp_CA_CP <= 0):
    flag = 1
    print("Точка лежит в треугольнике")
else:
    flag = 0
    print("Точка лежит вне треугольника")
# ищем векторы AP BP CP
AP_vektor_x = Px - Ax
AP_vektor_y = Py - Ay
BP_vektor_x = Px - Bx
BP_vektor_y = Py - By
CP_vektor_x = Px - Cx
CP_vektor_y = Py - Cy
# ищем длины AP BP CP, чтобы понять какая сторона треугольника наиболее удаленная от т. P 
AP = math.sqrt(pow(AP_vektor_x, 2) + pow(AP_vektor_y, 2))
BP = math.sqrt(pow(BP_vektor_x, 2) + pow(BP_vektor_y, 2))
CP = math.sqrt(pow(CP_vektor_x, 2) + pow(CP_vektor_y, 2))
# если точка P лежит внутри треугольника, то в зависимости от того какая из сторон треуголника наиболее удаленная от т. P  ищется расстояние от т. P до этой стороны
if (flag == 1):
    max_temp = AP
    if (BP > CP):
        dlina = AB
    else:
        dlina = CA
    if (BP > max_temp):
        max_temp = BP
        if (AP > CP):
            dlina = AB
        else:
            dlina = BC
    if (CP > max_temp):
        max_temp = CP
        if (AP > BP):
            dlina = CA
        else:
            dlina = BC
    if (dlina == AB):
        height = math.sqrt(pow(AB_vektor_x * AP_vektor_y, 2) + pow(AB_vektor_y * AP_vektor_x, 2)) / dlina
    if (dlina == BC):
        height = math.sqrt(pow(BC_vektor_x * BP_vektor_y, 2) + pow(BC_vektor_y * BP_vektor_x, 2)) / dlina
    if (dlina == CA):
        height = math.sqrt(pow(CA_vektor_x * CP_vektor_y, 2) + pow(CA_vektor_y * CP_vektor_x, 2)) / dlina
    print("Расстояние до самой удаленной стороны треугольника = ", f"{height:.6}")
    # вводятся координаты новой точки
Mx = int(input("Введите координату второй дополнительной точки по о.X: "))
My = int(input("Введите координату второй дополнительной точки по о.Y: "))
# цикл для проверки каждой стороны треугольника
for i in range(3):
    if i == 0:
        x1, y1, x2, y2 = Ax, Ay, Bx, By
    elif i == 1:
        x1, y1, x2, y2 = Bx, By, Cx, Cy
    else:
        x1, y1, x2, y2 = Cx, Cy, Ax, Ay
    # вычисление коэффициентов для первой прямой (однаииз сторон треугольника)
    A1 = y2 - y1
    B1 = x1 - x2
    C1 = A1 * x1 + B1 * y1
    # вычисление коэффициентов для MP
    A2 = My - Py
    B2 = Px - Mx
    C2 = A2 * Px + B2 * Py
    # вычисление определителя (из 4-х элементов)
    det = A1 * B2 - A2 * B1
    if det != 0:
        # вычисление точки пересечения по формуле Крамера
        x = (C1 * B2 - C2 * B1) / det
        y = (A1 * C2 - A2 * C1) / det
        # проверка, что точка пересечения принадлежит обоим отрезкам
        if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(Px, Mx) <= x <= max(Px,
                                                                                                           Mx) and min(
                Py, My) <= y <= max(Py, My):
            print("Прямая MP пересекает сторону треугольника в точке:", f"({x:.6})", f"({y:.6})")
            break
else:
    print("Прямая MP не пересекает треугольник ABC.")
