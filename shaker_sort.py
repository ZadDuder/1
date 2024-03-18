#Тымчишин. Шейкер-сортировка. ИУ7-11Б.
from random import randint
import timeit

def shaker_sort(arr):
    n = len(arr)
    change_count = 0
    swapped = True
    i = 0
    while swapped:
        swapped = False
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swapped = True
                change_count += 1
        
        if not swapped:
            break
        i +=1
        swapped = False
        for j in range(n-i-2, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                change_count += 1
                swapped = True
        
        i += 1
        print(arr)
    return arr, change_count

def generate_random_list(size):
    return [randint(-100, 100) for _ in range(size)]

# Блок ввода и сортировки пользовательского списка
while True:
    try:
        user_list = list(map(int, input("Введите числа для сортировки, разделенные пробелом: ").split()))
        sorted_user_list, _ = shaker_sort(user_list)
        print("Отсортированный пользовательский список:", sorted_user_list)
        break
    except ValueError:
        print("Ошибка: введите корректные целые числа.")

# Блок ввода размеров списков с обработкой исключений
while True:
    try:
        N1 = int(input("Введите размер первой последовательности N1: "))
        N2 = int(input("Введите размер второй последовательности N2: "))
        N3 = int(input("Введите размер третьей последовательности N3: "))
        break
    except ValueError:
        print("Ошибка: введите корректные целые числа.")

original_lists = {size: generate_random_list(size) for size in [N1, N2, N3]}
sorted_lists = {size: shaker_sort(original_lists[size][:])[0] for size in [N1, N2, N3]}

# Измерение времени и вывод таблицы результатов
results = {size: {'sorted': None, 'random': None, 'reversed': None} for size in [N1, N2, N3]}

for size in [N1, N2, N3]:
    for list_type in ['sorted', 'random', 'reversed']:
        if list_type == 'sorted':
            arr = list(range(size))
        elif list_type == 'random':
            arr = original_lists[size]
        else:
            arr = list(range(size, 0, -1))

        # Измеряем время и делаем перестановки
        t = timeit.timeit('shaker_sort(arr.copy())', globals=globals(), number=1)
        c = shaker_sort(arr.copy())[1]

        results[size][list_type] = (t, c)

# Выводим заголовок таблицы
header_format = "{:<20} {:<20} {:<20}"
header = header_format.format("Список", "Время (секунды)", "Перестановки")
print(header)

# Выводим результаты
for size in [N1, N2, N3]:
    print(f"{'-' * 60}")
    for list_type in ['sorted', 'random', 'reversed']:
        t, c = results[size][list_type]
        print(header_format.format(f"N{size} {list_type}", f"{t:.6f}", c))

# Выводим информацию о введенных и отсортированных списках
#for i, size in enumerate([N1, N2, N3], start=1):
#    original_list = original_lists[size]
#    sorted_list = sorted_lists[size]
#    print(f"Отсортированный сгенерированный список {i}: {sorted_list}")
