def log_count(file_path): # считает количество логов
    with open(file_path, 'r', encoding='utf-8') as file:
        counter = 0
        for line in file:
            counter += 1
    return counter
def PHP_answers(file_path): #  считает количество PHP кодов 200 404 302
    with open(file_path, 'r', encoding='utf-8') as file:
        counter_200 = 0
        counter_404 = 0
        counter_302 = 0
        for line in file:
            line = line.strip().split()
            if line[4] == '"200"': counter_200 += 1
            if line[4] == '"404"': counter_404 += 1
            if line[4] == '"302"': counter_302 += 1
    return counter_200, counter_404, counter_302
def clean_data(file_path: str) -> list[str]:
    with open(file_path, 'a', encoding='utf-8') as file:
        new_file_path = []
        for line in file:
            new_line = []
            for i in range(len(line)):
                if i == '"': continue
                else: new_line.append(i)
            new_file_path.append(new_line)
    return new_file_path

def biggest_answer(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        biggest_answ = 0
        main_line = -1
        for line in file:
            line = line.strip().split()
            if int(line[5]) > biggest_answ: biggest_answ = line[5], main_line = ' '.join(line)
    return main_line


file_path = 'logs.txt'
print(log_count(file_path))
print()
for i in range(0,3):
    print(PHP_answers(file_path)[i])
print()
print(clean_data(file_path))
