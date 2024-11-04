# Ввод от пользователя в минутах
tot_min = int(input("Введите число в минутах: "))

# Конвертация
hours = tot_min // 60
minutes = tot_min % 60

# Сбор данных и форматирование
# ИСПРАВИТЬ: вывод не соответствует требуемому формату (лишний символ конца строки, лишний текст)
# ИСПРАВЛЕНИЕ: Сделал в соответсвии с форматом задания
output = f"{tot_min} мин - это {hours} час {minutes} мин"

# Вывод результата
print(output)

# КОММЕНТАРИЙ: на текущем этапе инспектировать код было бы гораздо удобнее без функций
# КОММЕНТАРИЙ: Хорошо, тогда будем без функций


#================================
# Результат выполненой программы
#================================    
# D:\Ilya\Working\Bobkov\2024.10.27>python -i 3.py
# Введите число в минутах: 150
# 150 мин - это 2 час 30 мин
# >>> tot_min
# 150
# >>> hours
# 2
# >>> minutes
# 30


# ИТОГ: доработать — 2/4

