text = 'Мне сегодня 5 лет, мне 5 сегодня, мне 5... мне 5 лет!! сегодня'
new_text = ''
password = input("Введите пароль: ") 
key = '1'
for char in text:
    new_char = chr(ord(char) + ord(key))
    new_text += new_char
print(f"Зашифрованный текст: " + new_text)

if password == key:
    new_text_1 = ''
    for char in new_text:
        new_char_1 = chr(ord(char) - ord(password))
        new_text_1 += new_char_1
    print(f"Дешифрованный текст: " + new_text_1)
#else: print("Не взламывай мой пароль!!!")
if password != key:
    for i in range(1, 112064):
        if chr(str(i)) == chr(key): 
            print("Ключ найден, начинаю дешифровку...")
            new_text_1 = ''
            for char in new_text:
                new_char_1 = chr(ord(char) - ord())
                new_text_1 += new_char_1
            print(f"Дешифрованный текст: " + new_text_1)
            break
