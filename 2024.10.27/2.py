def main():
    num = int(input("Введите число: "))
    
    next_number = num + 1
    previous_number = num - 1
    
    output = f"""
Следущее за числом {num} число: {next_number}
Для число {num} предыдущее число: {previous_number}"""
    
    print(output)
    
    return num,output, next_number, previous_number
    
if __name__ == "__main__":
    num, output, next_number, previous_number = main()

#=============================================
# Это результат в интерактивном режиме
#=============================================

# D:\Ilya\Working\Bobkov\2024.10.27>python -i 2.py
# Введите число: 30

# Следущее за числом 30 число: 31
# Для число 30 предыдущее число: 29
# >>> num
# 30
# >>> next_number
# 31
# >>> previous_number
# 29
# >>> print(output)

# Следущее за числом 30 число: 31
# Для число 30 предыдущее число: 29
# >>>

#=============================================
# Я конечно, не имею большого опыта ООП, но когда я хотел сделать задание через перегрузку, оказывается в Python нужно создавать для этого классы, что как по мне неудобно. Этот вариант я сделал для себя, как метод практики с классами.
#=============================================

# class MyInteger:
   # def __init__(self, value):
     # self.value = value
     
   # def __add__(self, value):
     # return MyInteger(self.value + 1)
     
   # def __sub__(self, value):
     # return MyInteger(self.value - 1)
     
   # def __str__(self):
     # return str(self.value)
    
# def main():    
    # num = int(input("Введите число: "))
    # my_integer = MyInteger(num)
    
    # output=(
           # f"\nСледущее за числом {my_integer.value} число: {my_integer + 0}\n"
           # f"Для числа {my_integer.value} предыдущее число: {my_integer - 0}"
           # )
    # print(output)
# if __name__ == "__main__":
    # main()