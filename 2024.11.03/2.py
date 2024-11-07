def main():
    n = int(input('Введите количество цифр: ')) # Ввод данных
    total_sum = 0 # Это переменная для суммирования сюда положительных чисел
    
    # Запускаем цикл проверки и добавляем каждый раз, когда число положительно
    for _ in range(n):
        digit_input = int(input())
        if digit_input > 0:
            total_sum += digit_input
    print(total_sum)
    
main()

# D:\Ilya\Working\Bobkov\2024.11.03>python 2.py
# Введите количество цифр: 7
# 6
# 3
# -5
# 1
# 10
# -1
# 8
# 28