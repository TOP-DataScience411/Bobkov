def main():
    # Создание пустого списка
    listen = []
    # Входим в цикл и добавляем каждое число, введенное пользователем
    while True:
        data = int(input())
        if data % 7 == 0:
            listen.append(data)
            continue
        else:
            break
    # После прерывания, выводим каждое введенное число в инверсионном порядке
    for i in reversed(listen):
        print(i, end=' ')
        
main()


# D:\Ilya\Working\Bobkov\2024.11.03>python 1.py
# 7
# 14
# 21
# 28
# 29
# 28 21 14 7