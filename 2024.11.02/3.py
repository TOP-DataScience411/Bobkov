def leap_cheker(year):
    # Проверяем год
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    # Запрашиваем год у пользователя
    year = int(input("Введите год: "))
    
    # Проверка после выполнения функции
    if leap_cheker(year):
        print("Да")
    else:
        print("Нет")
        
main()



# D:\Ilya\Working\Bobkov\2024.11.02>python 3.py
# Введите год: 2020
# Да
# 
# D:\Ilya\Working\Bobkov\2024.11.02>python 3.py
# Введите год: 1846
# Нет