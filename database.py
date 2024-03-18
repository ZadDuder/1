#Тымчишин ИУ7-11Б 12 лаба
from typing import List


text = "На другой день после приема в ложу Пьер сидел дома, читая книгу и стараясь вникнуть в значение квадрата, изображавшего одной своей стороною Бога, другою нравственное, третьею физическое и четвертою смешанное. Изредка он отрывался от книги и квадрата и в воображении своем составлял себе новый план жизни. Вчера в ложе ему сказали, что до сведения государя 9/3 дошел слух о дуэли и что Пьеру благоразумнее было бы удалиться 9*8 из Петербурга. Пьер предполагал ехать в свои южные 5*3 имения и заняться там своими крестьянами. Он радостно обдумывал эту новую жизнь, когда неожиданно в комнату вошел князь Василий. — Мой друг, что ты наделал в Москве? За что ты поссорился с Лелей, mon cher? Ты в 20/2 заблуждении, — сказал князь Василий, входя в комнату. — Я все узнал, я могу тебе сказать верно, что Элен невинна перед тобой, как Христос перед жидами."
current_text = text
def formating(text):
    len_line = round(len(text) / 10)
    lines = []
    line = ""
    for word in text.split():
        if len(word+line) > len_line:
            lines.append(line)
            line = ""
        line += " " + word
    lines.append(line)   
    return lines

def right_align(lines):
    max_len_line = 0
    for el in lines:
        if len(el) > max_len_line:
            max_len_line = len(el)
    for i in range(len(lines)):
        lines[i] = " "*(max_len_line - len(lines[i])) + lines[i]

def width_align(lines):
    # Находим максимальную длину строки среди всех строк
    max_len_line = max(len(line) for line in lines)

    # Перебираем каждую строку в списке lines
    for index, line in enumerate(lines):
        # Разбиваем строку на слова
        words = line.split()
        # Если в строке только одно слово, выравниваем его по левому краю
        if len(words) == 1:
            lines[index] = words[0].ljust(max_len_line)
            continue
        # Вычисляем общее количество необходимых пробелов
        total_spaces_needed = max_len_line - len(line) + (len(words) - 1)
        # Вычисляем количество пробелов между словами
        spaces_per_gap = total_spaces_needed // (len(words) - 1)
        # Вычисляем количество дополнительных пробелов
        extra_spaces = total_spaces_needed % (len(words) - 1)
        # Начинаем формировать новую строку с первого слова
        new_line = words[0]
        # Добавляем пробелы и слова в новую строку
        for i in range(1, len(words)):
            # Добавляем дополнительный пробел в начало строки, пока они не закончатся
            space = ' ' * (spaces_per_gap + (1 if i <= extra_spaces else 0))
            new_line += space + words[i]
        # Обновляем строку в списке lines
        lines[index] = new_line
    # Возвращаем обновленный список lines
    return lines

def delete_word(lines, key):
    new_lines = []  # Создаем новый список для хранения обновленных строк
    for line in lines:
        new_line = ' '.join([word for word in line.split() if word != key])
        new_lines.append(new_line)
    return new_lines

def change_word(lines, key, lock):
    new_lines = []  # Создаем новый список для хранения обновленных строк
    for line in lines:
        new_line = []
        #new_line = ' '.join([word for word in line.split() if word != key])
        for word in line.split(): 
            if word != key: new_line.append(word)
            if word == key: new_line.append(lock)
        new_lines.append(new_line)
    return new_lines

def searching_numbers(lines: List[str]) -> List[str]:
    new_lines = []
    sign = '*/'
    for line in lines:
        new_line = []
        for word in line.split():
            now_sign = ''
            if '*' or '/' in word:
                word_copy = list(word)
                for i in range(len(word_copy)):
                    if word_copy[i] in sign: 
                        now_sign = word_copy[i]
                        ind_sign = i
                        num_1 = int(''.join([word_copy[i] for i in range(len(word_copy)) if i < ind_sign]))
                        num_2 = int(''.join([word_copy[i] for i in range(len(word_copy)) if i > ind_sign]))
                if now_sign == '*': 
                    word = str(num_1 * num_2)
                if now_sign == '/': 
                    word = str(num_1 / num_2)
            new_line.append(word)
        new_lines.append(new_line)
    return new_lines

def gl_max(text):
    gl = 'уеыаоэяиюУЕЫАОЭЯИЮ'
    points = text.split(".")
    max_gl = 0
    main_point = "" 
    for point in points:
        counter = 0
        for symbol in point:
            if symbol in gl:
                counter += 1
        if counter > max_gl:
            max_gl = counter
            main_point = point
    new_text = []
    for point in points:
        if point == main_point: continue
        else: new_text.append(point)
    return main_point, new_text




while True:
    print("Доступные команды:" + "\n0 - завершение" + "\n1 - выравнивание по левому краю" +
          "\n2 - выравнивание по правому краю" + "\n3 - выравнивание по ширине" +
          "\n4 - удаление слова" + "\n5 - замена слова" + "\n6 - посчитать арифметические выражения" +
          "\n7 - удаление предложения с наибольшим кол-вом гласных")

    try:
        user_choose = int(input("Введите команду: "))
    except ValueError:
        print("Введено не число. Попробуйте снова.")
        continue

    if user_choose == 0:
        break

    if user_choose == 1:
        lines = formating(current_text)
        current_text = "\n".join(lines)
        print(current_text)
    elif user_choose == 2:
        lines = formating(current_text)
        right_align(lines)
        current_text = "\n".join(lines)
        print(current_text)
    elif user_choose == 3:
        lines = formating(current_text)
        current_text = "\n".join(width_align(lines))
        print(current_text)
    elif user_choose == 4:
        lines = formating(current_text)
        key = input("Введите удаляемое слово: ")
        current_text = "\n".join(delete_word(lines, key))
        print(current_text)
    elif user_choose == 5:
        lines = formating(current_text)
        key = input("Введите слово, которое нужно заменить: ")
        lock = input("Введите слово, которым нужно заменить: ")
        current_text = "\n".join([" ".join(a) for a in change_word(lines, key, lock)])
        print(current_text)
    elif user_choose == 6:
        lines = formating(current_text)
        current_text = "\n".join([" ".join(a) for a in searching_numbers(lines)])
        print(current_text)
    elif user_choose == 7:
        gl_max_result = gl_max(current_text)
        print(f"Искомое предложение: {gl_max_result[0]}\n")
        current_text = "\n".join(gl_max_result[1])
        print(current_text)
