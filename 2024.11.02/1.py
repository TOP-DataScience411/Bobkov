def main():
    while True:
        # Ввод пользователя
        numbers = input().strip().split()
        valid_numbers = []
        
        # Проверка на ввод
        for num in numbers:
            try:
               valid_numbers.append(float(num))
            except ValueError:
               print('Число не корректно, попробуйте снова')
               break
        if len(valid_numbers) != 3:
            print('Вы ввели не три числа')
            continue
        
        # Присвоение с проверкой
        pos_num = [num for num in valid_numbers if num > 0]
        
        # Проверка количества положительных чисел
        if len(pos_num) < 2:
            print('Недостаточно чисел для суммирования.')
        else:
            summ = sum(pos_num)
            print(summ)
        break

main()


# D:\Ilya\Working\Bobkov\2024.11.02>python 1.py
# 
# 4 -22 1.5
# 5.5