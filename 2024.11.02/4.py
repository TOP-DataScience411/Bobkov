import sys

def create_CHB():
    # Создаем доску
    chess_board = [
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    ]
    return chess_board
    
def check_board_info(board, cell):
    # Проверка правильности длинны
    if len(cell) != 2:
        return 'Вы ввели некорректно, пример [a2]'
    
    # Проверка на диапазон
    if cell[0] < 'a' or cell[0] > 'h':
        return 'Первая буква должна быть в диапазоне от a до h.'
    else:
        column = ord(cell[0]) - ord('a')
            
    # Попытка перевести в целочисленное
    try:
        row = int(cell[1]) - 1
        if row < 0 or row > 7:
            return 'Ваши данные находятся за пределами шахматной доски'
    except ValueError:
        return 'Вы должны ввести числа'
        
    # Проверка на вхождение внутри доски, если проходит, получаем данные о клетке
    if 0 <= column < 8 and 0 <= row < 8:
        color = board[row][column]
        return color
    
def main():
    chess_board = create_CHB()
    
    # Входим в цикл, где берем введенные данные и проверяем, что введены две координаты
    while True:
        input_data = sys.stdin.readline().strip().lower()
        cells = input_data.split()
        
        if len(cells) != 2:
            print('Вы ввели не две координаты')
        else:
            break
    
    # Запускаем функцию проверки и забираем оттуда цвет
    color1 = check_board_info(chess_board, cells[0])
    color2 = check_board_info(chess_board, cells[1])
    
    # Отладочный код, который показывает содержимое выбранной клетки
    print(f"Цвет клетки {cells[0]}: {color1}")
    print(f"Цвет клетки {cells[1]}: {color2}")
    
    # Проверяем соотношение двух выбранных клеток
    if color1 == color2:
        print('Да')
    else:
        print('Нет')
        
main()



# D:\Ilya\Working\Bobkov\2024.11.02>python 4.py
# a1 b5
# Цвет клетки a1: B
# Цвет клетки b5: W
# Нет
# 
# D:\Ilya\Working\Bobkov\2024.11.02>python 4.py
# a1 b2
# Цвет клетки a1: B
# Цвет клетки b2: B
# Да