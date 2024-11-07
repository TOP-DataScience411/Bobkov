def telegramm_sum(message):
    chars = len(message)
    
    cost = 30
    
    sum_cost = cost * chars
    
    rub = sum_cost // 100
    kop = sum_cost % 100
    
    return rub, kop

def main():
    message = input()
    
    rub, kop = telegramm_sum(message)
    print(f"{rub} руб. {kop} коп.")
    
main()


# D:\Ilya\Working\Bobkov\2024.11.03>python 5.py
# Какой-то новогодний вечер
# 7 руб. 50 коп.