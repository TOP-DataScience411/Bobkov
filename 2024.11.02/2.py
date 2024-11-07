import sys

def main():
    try:
        #Регистрируем ввод
        input_data = sys.stdin.readline().strip().split()
        
        # Распаковка
        num1  = int(input_data[0])
        num2  = int(input_data[1])
        
        # проверка деления, в том числе на ноль
        if num2 == 0:
            print('Нельзя делить на ноль!')
        elif  num1 % num2 == 0:
            print(f'{num1} делится на {num2} без остатка\nЦелое {num1//num2}')
        else:
            print(f'{num1} не делится на {num2} без остатка\nЦелое: {num1//num2}\nОстаток: {num1%num2}')
    except ValueError:
        print('Вы ввели не числа')
    except IndexError:
        print('Вы ввели сколько чисел?')
        
main()


# D:\Ilya\Working\Bobkov\2024.11.02>python 2.py
# 8 2
# 8 делится на 2 без остатка
# Целое 4
# 
# D:\Ilya\Working\Bobkov\2024.11.02>python 2.py
# 10 3
# 10 не делится на 3 без остатка
# Целое: 3
# Остаток: 1