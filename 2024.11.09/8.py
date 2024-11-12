def search_names(data):
    # Разделяем входную строку на имена файлов
    files = data.split('; ')
    
    # Словарь для отслеживания количества встреченных полных имен файлов
    file = {}
    # Список для хранения переименованных файлов
    file_rename = []
    
    
    for f in files:
        # Проверяем, есть ли расширение у файла
        if '.' in f:
            # Разделяем имя файла на имя и расширение
            name, ext = f.rsplit('.', 1)
        else:
            name, ext = f, '' # Если точки нет, то расширение пустое
                
        # Проверяем наличие полного имени файла в словаре
        if f in file:
            file[f] += 1 # Увеличиваем счётчик для дублирующегося файла
            # Формируем новое имя с суффиксом
            new = f"{name} ({file[f]})"
            if ext: # Если есть расширение, добавляем его обратно
                new += f".{ext}"
            file_rename.append(new)  # Добавляем новое имя в список
        else:
            file[f] = 1 # Впервые встречаемый файл
            file_rename.append(f)  # Добавляем оригинальное имя в список
    
    return file_rename

def main():
    input_data = input("Введите файлы через этот паттерн(; ):")
    
    result = search_names(input_data)  # Получаем переименованные файлы
    
    # Выводим результаты
    for name in result:
        print(name)
        
main()


# D:\Ilya\Working\Bobkov\2024.11.09>python 8.py
# Введите файлы через этот паттерн(; ):1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz; 1.txt
# 1.py
# 1 (2).py
# src.tar.gz
# aux.h
# main.cpp
# functions.h
# main (2).cpp
# 1 (3).py
# main (3).cpp
# src.tar (2).gz
# 1.txt