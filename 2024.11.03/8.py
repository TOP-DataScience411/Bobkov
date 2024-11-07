def fibonacci(n):
    fib_list = []
    a, b = 1, 1
    
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
        
    return fib_list

def main():
    n = int(input("Введите число Фибоначи: "))
    
    if n <= 0:
        print("Пожалуйста, введите натуральное число.")
    
    fibo = fibonacci(n)
    
    print(fibo)
    
main()

# D:\Ilya\Working\Bobkov\2024.11.03>python 8.py
# Введите число Фибоначи: 1
# [1]
# 
# D:\Ilya\Working\Bobkov\2024.11.03>python 8.py
# Введите число Фибоначи: 17
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]