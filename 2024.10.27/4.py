def main():
    # Ввод пользователя и проверка на трехзначность
    while True:
        number = int(input("Введите 3-значное число:"))
        if 100 <= number <= 999:
            break
        else:
            print("Ошибка: введите трехзначное число!")
    
    # Инициализация процесса
    sum_num = 0
    prod_num = 1
    
    # Извлекаем каждую цифру
    for _ in range(3):
       digit = number % 10
       sum_num += digit
       prod_num *= digit
       number //= 10
    
    # Вывод результата
    print(f"Сумма цифр: {sum_num}")
    print(f"Произведение цифр: {prod_num}")
    
    return sum_num, prod_num
if __name__ == "__main__":
    sum_num, prod_num = main()
    
# Я не вывожу переменную number по той причине, что с ней проводятся вычисления и какое бы значение не было введено пользователем, будет равна 0

# D:\Ilya\Working\Bobkov\2024.10.27>python -i 4.py
# Введите 3-значное число:666
# Сумма цифр: 18
# Произведение цифр: 216
# >>> sum_num
# 18
# >>> prod_num
# 216
# >>>