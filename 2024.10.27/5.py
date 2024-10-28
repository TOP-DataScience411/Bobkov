def main():
    # Ввод данных от пользователя
    imiles = int(input("Введите целое число мили: "))
    fmiles = int(input("Введите дробное число мили: "))
    
    # Объединение в одно
    fusemiles = imiles + (fmiles / 10)
    
    # Конвертация в км
    Kilometers = fusemiles * 1.61
    
    # сокращение
    rkm = round(Kilometers, 2)
    
    # Вывод результата
    print(f"{fusemiles} миль = {rkm} километров")
    
if __name__ == "__main__":
    main()

# Здесь я не заморачивался с инспекцией, в принципе, тут и так понятно
    
# D:\Ilya\Working\Bobkov\2024.10.27>python 5.py
# Введите целое число мили: 15
# Введите дробное число мили: 7
# 15.7 миль = 25.28 километров

# D:\Ilya\Working\Bobkov\2024.10.27>