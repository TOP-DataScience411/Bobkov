import math

def sum_iterations(n):
    total_sum = 0
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total_sum += i
            if i != n // i:
                total_sum += n // i
    return total_sum
    
def main():
    n = int(input("Введите натуральное число: "))
    
    summ = sum_iterations(n)
    print(summ)

main()

# D:\Ilya\Working\Bobkov\2024.11.03>python 3.py
# Введите натуральное число: 50
# 93
# 