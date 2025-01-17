def main():
    # КОММЕНТАРИЙ: пример плохочитаемой и негибкой структуры условно-бесконечного цикла
    while True:
        # Ввод пользователя
        # КОММЕНТАРИЙ: если вы запрашиваете ввод всех чисел в одну строчку, то на что вам вообще сдался условно-бесконечный цикл?
        numbers = input().strip().split()
        valid_numbers = []
        
        # Проверка на ввод
        for num in numbers:
            try:
               valid_numbers.append(float(num))
            except ValueError:
               print('Число не корректно, попробуйте снова')
               break
        
        # КОММЕНТАРИЙ: проблема в том, что вы запрашиваете данные пакетом (в одну строчку), и если не соблюдено требование к вводу, то отбрасываете весь пакет, вынуждая пользователя заново отправлять весь пакет (повторять весь ввод целиком)
        if len(valid_numbers) != 3:
            print('Вы ввели не три числа')
            continue
        
        # КОММЕНТАРИЙ: обработка результатов ввода должна быть за пределами условно-бесконечного цикла
        # Присвоение с проверкой
        pos_num = [num for num in valid_numbers if num > 0]
        # КОММЕНТАРИЙ: это требование вы тоже сами придумали, в задаче его не было
        # Проверка количества положительных чисел
        if len(pos_num) < 2:
            # КОММЕНТАРИЙ: пичалька... ведь теперь вы не можете даже повторить ввод, чтобы соблюсти и это требование, ваша программа просто завершает работу так ничего полезного и не сделав
            print('Недостаточно чисел для суммирования.')
        else:
            summ = sum(pos_num)
            print(summ)
        break


main()


# D:\Ilya\Working\Bobkov\2024.11.02>python 1.py
# 
# 4 -22 1.5
# 5.5


# КОММЕНТАРИЙ: на занятии по циклам я показывал, как оформлять условно-бесконечный запрос данных, пока не будут удовлетворены требования к вводу — сравните тот код с этим своим

