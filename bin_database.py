# Тымчишин ИУ7-11Б. Бин БД и операции над ней
import struct

# БД вида: ID "кол-во товара" цена

filename = 'test_data.bin'

def create_bindata(filename, records):  # создает бд по переданному ей списку
    with open(filename, 'wb') as file:
        for el in records:
            num1 = struct.pack('f', float(el[0]))
            num2 = struct.pack('f', float(el[1]))
            num3 = struct.pack('f', float(el[2]))
            file.write(num1)
            file.write(num2)
            file.write(num3)

def data_out(filename):  # выводит бд
    with open(filename, 'rb') as file:
        while True:
            bytes_data1 = file.read(12)
            if not (bytes_data1):
                break
            el1 = struct.unpack('3f', bytes_data1)[0]
            el2 = struct.unpack('3f', bytes_data1)[1]
            el3 = struct.unpack('3f', bytes_data1)[2]
            print(el1, el2, el3)

import os

def insert_record(filename, position, record):  # вставка в бд
    record = record.split()
    filesize = os.path.getsize(filename)
    with open(filename, 'r+b') as file:  # не спрашивайте почему это работает, я и сам не до конца знаю)
        for i in range(filesize, position * 12, -12):
            file.seek(i - 12)
            bytes_data = file.read(12)
            file.seek(i)
            file.write(bytes_data)
        file.seek(position * 12)
        for value in record:
            file.write(struct.pack('f', float(value)))

def delete_record(filename, position):
    filesize = os.path.getsize(filename)
    with open(filename, 'r+b') as file:
        for i in range(position * 12, filesize - 12, 12):
            file.seek(i + 12)
            bytes_data = file.read(12)
            file.seek(i)
            file.write(bytes_data)
        file.truncate(filesize - 12)

def search_by_id(filename, target_id):  # посик по ид
    with open(filename, 'rb') as file:
        found = False
        while True:
            bytes_data = file.read(12)
            if not bytes_data:
                break
            record = struct.unpack('3f', bytes_data)
            if record[0] == target_id:
                print(f"Найдена запись: ID = {record[0]}, Количество = {record[1]}, Цена = {record[2]}")
                found = True
        if not found:
            print("Записи с таким ID не найдены")

def search_by_quantity_and_price(filename, target_quantity, target_price):
    with open(filename, 'rb') as file:
        found = False
        while True:
            bytes_data = file.read(12)
            if not bytes_data:
                break
            record = struct.unpack('3f', bytes_data)
            if record[1] == target_quantity and record[2] == target_price:
                print(f"Найдена запись: ID = {record[0]}, Количество = {record[1]}, Цена = {record[2]}")
                found = True
        if not found:
            print("Записи с такими параметрами не найдены")

while True:
    print("Доступные команды:")
    print("1 - Выбор базы данных")
    print("2 - Создание базы данных")
    print("3 - Вывод базы данных")
    print("4 - Вставка строки в указанное место")
    print("5 - Удаление указанной строки")
    print("6 - Поиск по ID")
    print("7 - Поиск по количеству товара и цене")
    try:
        user_in = int(input("Ваша команда: "))
    except ValueError:
        print("Введено не число. Попробуйте снова!")
        continue
    if int(user_in) == 0: break
    if int(user_in) == 1:
        print("При вводи полного пути, символ \\ дублируйте")
        filename = input("Введите имя файла: ")
        open(filename, 'ab').close()
    if int(user_in) == 2:
        #создание/перезапись бд
        records = []
        print("Напоминание: БД вида: (ID) (кол-во товара) (цена)")
        print("Для завершения ввода нажмите enter")
        while True: 
            line = input("Введите строку бд через пробел: ")
            if line: records.append(line.split())
            else: break
        create_bindata(filename, records)
    if int(user_in) == 3: 
        #вывод бд
        data_out(filename)
    if int(user_in) == 4:
        #вставка в бд
        try:
            position = int(input("Введите ID для вставки: "))
        except ValueError:
            print("Введено не число. Попробуйте снова!")
            continue
        record = input("Введите строку для вставки в бд: ")
        insert_record(filename, position, record)
    if int(user_in) == 5:
        try:
            position = int(input("Введите ID удаляемой строки: "))
        except ValueError:
            print("Введено не число. Попробуйте снова!")
            continue
        delete_record(filename, position)
    if int(user_in) == 6:
        try:
            target_id = int(input("Введите искомый ID: "))
        except ValueError:
            print("Введено не число. Попробуйте снова!")
            continue
        search_by_id(filename, target_id)
    if int(user_in) == 7:
        try:
            target_quantity = float(input("Введите искомое количество товара: "))
            target_price = float(input("Введите искомую цену: "))
        except ValueError:
            print("Введено не число. Попробуйте снова!")
            continue            
        search_by_quantity_and_price(filename, target_quantity, target_price)
# комментарий