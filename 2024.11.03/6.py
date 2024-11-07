def lucky_ticket(ticket):
    if len(ticket) == 6:
        dticket = list(map(int, ticket))
        n1 = sum(dticket[:3])
        n2 = sum(dticket[3:])
        if n1 == n2:
            return "Да"
        else:
            return "Нет"
    else:
        return "Ошибка, вы ввели неверное число"

def main():
    ticket = input("Введите ваш билет(6-значный): ")
    
    result = lucky_ticket(ticket)
    print(result)
    
main()


# D:\Ilya\Working\Bobkov\2024.11.03>python 6.py
# Введите ваш билет(6-значный): 183534
# Да
# 
# D:\Ilya\Working\Bobkov\2024.11.03>python 6.py
# Введите ваш билет(6-значный): 401367
# Нет