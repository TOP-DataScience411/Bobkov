def check_rook_move(start, end):
    # Преобразование полученных координат
    start_col = ord(start[0]) - ord('a')
    start_row = int(start[1]) - 1
    end_col = ord(end[0]) - ord('a')
    end_row = int(end[1]) - 1
    
    # Проверка на вхождение в диапазон доски
    if not (0 <= start_col < 8 and 0 <= start_row < 8 and 0 <= end_col < 8 and 0 <= end_row < 8):
        return 'Вы пытаетесь применить координаты за пределами доски'
    
    # Вертикальная и горизонтальная проверки с возвращением результата
    if start_col == end_col:
        step = 'Да' if end_row > start_row or end_row < start_row else 'Нет'
        return step
    elif start_row == end_row:
        step = 'Да' if end_col > start_col or end_col < start_col else 'Нет'
        return step
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
            start = input_data[0]
            end = input_data[1]
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
    step = check_rook_move(start, end)
    print(step)
    
main()

# D:\Ilya\Working\Bobkov\2024.11.02>python 5.py
# Введите координаты через пробел:d4 e4
# Да
# 
# D:\Ilya\Working\Bobkov\2024.11.02>python 5.py
# Введите координаты через пробел:a2 c4
# Нет