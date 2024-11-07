def check_king_move(start, end):
    # Преобразование полученных координат
    start_col = ord(start[0]) - ord('a')
    start_row = int(start[1]) - 1
    end_col = ord(end[0]) - ord('a')
    end_row = int(end[1]) - 1
    
    # Проверка на вхождение в диапазон доски
    if not (0 <= start_col < 8 and 0 <= start_row < 8 and 0 <= end_col < 8 and 0 <= end_row < 8):
        return 'Вы пытаетесь применить координаты за пределами доски'
    
    # Проверка, может ли король ходить в таком направлении
    if start_col == end_col and start_row == end_row:
        return 'Нет'
    else:
        if abs(end_col - start_col) <= 1 and abs(end_row - start_row) <= 1:
           return 'Да'
        else:
           return 'Нет'
        
        
def main():
    # Цикл с получением данных от пользователя и проверки, что введены правильно
    while True:
        input_data = input('Введите координаты через пробел:').strip().split()
        if len(input_data) != 2:
            print('Вы ввели не две координаты, пример: b5 b2')
            continue
        else:
            start, end = input_data
            if len(start) != 2 or len(end) != 2:
                print('Вы ввели неправильно, пример: b5 b2')
                continue
            else:
                if not (start[1].isdigit() and end[1].isdigit()):
                    print('Вторая часть координат должна быть числом от 1 до 8. Пример: b5 b2')
                    continue
                else:
                    break
    
    # Запуск функции проверки хода и получение результата
    step = check_king_move(start, end)
    print(step)
    
main()



# D:\Ilya\Working\Bobkov\2024.11.02>python 6.py
# Введите координаты через пробел:g3 f2
# Да
# 
# D:\Ilya\Working\Bobkov\2024.11.02>python 6.py
# Введите координаты через пробел:c6 d4
# Нет