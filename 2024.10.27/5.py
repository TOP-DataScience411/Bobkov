def main():
    # Ввод данных от пользователя
    # imiles = int(input("Введите целое число мили: "))
    # fmiles = int(input("Введите дробное число мили: "))
    
    # Объединение в одно
    # ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше одного (см. тест ниже) — придумайте более универсальное решение
    # ИСПРАВЛЕНИЕ: Так пойдет? Теперь можно использовать любую дробную длинну
    # leng = len(str(fmiles))
    # fusemiles = imiles + (fmiles / (10 ** leng))
    
    # ИСПОЛЬЗОВАТЬ: можно проще и с меньшим количеством вычислений:
    imiles = input("Введите целое число мили: ")
    fmiles = input("Введите дробное число мили: ")
    fusemiles = float(f'{imiles}.{fmiles}')
    
    # Конвертация в км
    kilometers = fusemiles * 1.61
    
    # Вывод результата
    # ИСПРАВИТЬ: вывод не соответствует требуемому формату (неверный текст)
    # ИСПРАВЛЕНИЕ: Хорошо, сделал в точности, как в текстовом задании
    print(f"{fusemiles} миль = {round(kilometers, 1)} км")
    
    return fusemiles, kilometers


if __name__ == "__main__":
    fusemiles, kilometers = main()


# Теперь инспектирование переменных
    
# D:\Ilya\Working\Bobkov\2024.10.27>python 5.py
# Введите целое число мили: 15
# Введите дробное число мили: 7
# 15.7 миль = 25.28 километров
# 
# D:\Ilya\Working\Bobkov\2024.10.27>

# Вторая интерпретация с инспекцией
# 
# D:\Ilya\Working\Bobkov\2024.10.27>python -i 5.py
# Введите целое число мили: 20
# Введите дробное число мили: 523545621
# 20.523545621 миль = 33.0 км
# >>> fusemiles
# 20.523545621
# >>> kilometers
# 33.04290844981


# Введите целое число мили: 5
# Введите дробное число мили: 81
# КОММЕНТАРИЙ: должно быть 5.81 миль
# 13.1 миль = 21.09 километров


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/


# ИТОГ: хорошо — 4/5

