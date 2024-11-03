first_name = ""
last_name = ""
birth_year = "" 

def main():
    global first_name, last_name, birth_year
    
    # Запрос данных у пользователя
    first_name = input("Ведите своё имя: ")
    last_name = input("Ведие своё фамилия: ")
    birth_year = input("Введите свой год рождения:")
    
    # Вывод данных, полученных от пользователя
    print("\nСобранные данные:")
    print("\nИмя:" + first_name)
    print("Фамилия:" + last_name)
    print("Год рождения:" + birth_year)
    
    # Пауза(Для отладки)
    input("\n Нажмите Enter, чтобы выйти... ")


if __name__ == "__main__":
    main()


# D:\Ilya\Working\Bobkov\2024.10.27>python -i 1.py
# Ведите своё имя: Илья
# Ведие своё фамилия: Бобков
# Введите свой год рождения:1991
# 
# Собранные данные:
# 
# Имя:Илья
# Фамилия:Бобков
# Год рождения:1991
# 
#  Нажмите Enter, чтобы выйти... pbd
# >>> first_name
# 'Илья'
# >>> last_name
# 'Бобков'
# >>> birth_year
# '1991'

