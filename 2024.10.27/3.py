def main():
    # Ввод от пользователя в минутах
    tot_min = int(input("Введите число в минутах: "))
    
    # Конвертация
    hours = tot_min // 60
    minutes = tot_min % 60
    
    # Сбор данных и форматирование
    output = f"\n{tot_min} количество минут равняется - {hours} часов {minutes} минут"
    
    # Вывод результата
    print(output)
    
    # Возвращение значений для возможности инспектирования
    return hours, minutes, tot_min


if __name__ == "__main__":
    hours, minutes, tot_min = main()


#================================
# Результат выполненой программы
#================================    
# D:\Ilya\Working\Bobkov\2024.10.27>python -i 3.py
# Введите число в минутах: 150
# 
# 150 количество минут равняется - 2 часов 30 минут
# >>> tot_min
# 150
# >>> hours
# 2
# >>> minutes
# 30
# >>>

