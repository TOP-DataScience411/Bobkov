def fruit_generator():
    while True:
        fruit = input("Введите фрукт: ")
        if fruit == "":
            break
        yield fruit

def main():
    fruits = set(fruit_generator())
    
    if fruits:
        fruit_list = list(fruits)
        if len(fruits) == 1:
            output = fruit_list[0]
        elif len(fruits) == 2:
            output = f"{fruit_list[0]} и {fruit_list[1]}"
        else:
            output = ", ".join(fruit_list[:-1]) + ' и ' + fruit_list[-1]
        print(output)
    else:
        print("Нечего выводить.")
            
main()


# D:\Ilya\Working\Bobkov\2024.11.09>python 2.py
# Введите фрукт: Манго
# Введите фрукт: Манго
# Введите фрукт: Киви
# Введите фрукт: Апельсин
# Введите фрукт: Киви
# Введите фрукт: Персик
# Введите фрукт:
# Манго, Киви, Персик и Апельсин