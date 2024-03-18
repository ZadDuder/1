import csv
filename = 'C:\\Users\\Egorik\\Desktop\\important_progs\\testik.csv'
with open(filename, 'r', encoding='windows-1251') as file:
        csv_reader = csv.reader(file)
        head_table = next(csv_reader)

def out_info(row: list):
    print("="*100)
    for i in range(0, len(head_table)):
        print(f"{head_table[i]} : {row[i]}")
    print("="*100)

def search_by_name(filename):
    print("Доступные ученики: ")
    with open(filename, 'r', encoding='windows-1251') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[len(head_table) - 1] == '1': print(row[0])
    key_name = input("Введите искомое имя: ")
    with open(filename, 'r', encoding='windows-1251') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == key_name: out_info(row)

def all_out(filename):
    with open(filename, 'r', encoding='windows-1251') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader: out_info(row)

while True:
    try:
        print("Доступные команды: ")
        print("0 - завершение \n1 - вывод всей баз данный \n2 - поиск по имени")
        user_choose = int(input("Введите команду: "))
        if user_choose == 0: break
        if user_choose == 1: pass
        if user_choose == 2: search_by_name(filename)
    except ValueError:
        print("Введите число")  
