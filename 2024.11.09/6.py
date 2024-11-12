def binary_check(inp):
    inp = inp.strip()
    
    if inp.startswith('0b'):
        inp = inp[2:]
    elif inp.startswith('b'):
        inp = inp[1:]
    
    valid_set = {'0', '1'}
    
    return len(inp) > 0 and all(char in valid_set for char in inp)
    
def main():
    input_data = input("Введите бинарное число: ").strip()
    
    if binary_check(input_data):
        print("Да")
    else:
        print("Нет")
        
main()


# D:\Ilya\Working\Bobkov\2024.11.09>python 6.py
# Введите бинарное число: b01001
# Да
# 
# D:\Ilya\Working\Bobkov\2024.11.09>python 6.py
# Введите бинарное число: 1b0101
# Нет