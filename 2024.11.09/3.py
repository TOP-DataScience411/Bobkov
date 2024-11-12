f_list = list(map(int, input("Ведите первый лист: ").split()))
s_list = list(map(int, input("Ведите второй лист: ").split()))

if len(f_list) > len(s_list):
    print("Нет, первый список больше второго.")
else:
    len_s = len(s_list)
    len_f = len(f_list)
    found = False
    
    for i in range(len_s - len_f + 1):
        match = True
        
        for j in range(len_f):
            if s_list[i+j] != f_list[j]:
                match = False
                break
        if match:
            found = True
            break
    if found:
        print("Да")
    else:
        print("Нет")

# D:\Ilya\Working\Bobkov\2024.11.09>python 3.py
# Ведите первый лист: 1 2 3
# Ведите второй лист: 1 2 3
# Да
# 
# D:\Ilya\Working\Bobkov\2024.11.09>python 3.py
# Ведите первый лист: 1 2 3 4
# Ведите второй лист: 3 4
# Нет, первый список больше второго.
# 
# D:\Ilya\Working\Bobkov\2024.11.09>python 3.py
# Ведите первый лист: 3 4
# Ведите второй лист: 1 2 3 4
# Да
# 
# D:\Ilya\Working\Bobkov\2024.11.09>python 3.py
# Ведите первый лист: 10 20 30
# Ведите второй лист: 10 30 40 50
# Нет