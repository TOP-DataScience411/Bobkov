def num_mmd(num_list: list, n: int=1, *, copy: bool=False) ->list[float]:
    if copy:
        num_list_new = num_list.copy()
        for _ in range(n):
            num_list_new.remove(min(num_list_new))
            num_list_new.remove(max(num_list_new))
        return num_list_new, num_list
    else:
        for _ in range(n):
            num_list.remove(min(num_list))
            num_list.remove(max(num_list))
        return num_list
        
# D:\Ilya\Working\Bobkov\2024.11.10>python -i 3.py
# >>> num_mmd([1, 2, 3, 4])
# [2, 3]
# >>> num_mmd([1, 5, 7, 10, 2, 4, 3, 8, 9], 2)
# [5, 7, 4, 3, 8]
# 
# >>> numbers = [12.5, 3.2, 45.7, 23.1, 67.8, 1.0, 34.5, 56.3, 89.9, 22.4, 15.6, 78.2, 4.4, 99.1, 8.8, 0.5, 37.6, 19.3, 6\6.0, 55.5]
# >>> num_mmd(numbers, 2)
# [12.5, 3.2, 45.7, 23.1, 67.8, 34.5, 56.3, 22.4, 15.6, 78.2, 4.4, 8.8, 37.6, 19.3, 66.0, 55.5]