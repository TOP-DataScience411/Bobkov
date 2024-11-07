def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
           return False
    return True

def count_primes(n):
    if n < 1:
        return 0
        
    mininal = 10 ** (n-1)
    maximal = 10**n - 1
    
    primes = 0
    
    for num in range(mininal, maximal + 1):
        if is_prime(num):
            primes += 1
            
    return primes

def main():
    n = int(input("Введите разрядность числа: "))
    
    result = count_primes(n)
    print(result)
    
main()


# D:\Ilya\Working\Bobkov\2024.11.03>python 4.py
# Введите разрядность числа: 3
# 143
# 
# D:\Ilya\Working\Bobkov\2024.11.03>python 4.py
# Введите разрядность числа: 5
# 8363