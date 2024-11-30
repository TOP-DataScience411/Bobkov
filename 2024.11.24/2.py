def multiplication(num):
    listp = list(num)
    if not listp:
        return 1.0
    return float(num[0] * multiplication(num[1:]))
    
    
# >>> multiplication([2, 5, 10])
# 100.0
# >>> multiplication([2, 5, 2.4])
# 24.0