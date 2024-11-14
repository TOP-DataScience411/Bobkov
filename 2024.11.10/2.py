def taxi_tax(distance: int, /, waiting: int = 0) -> int:
    if distance < 0 or waiting < 0:
        return None
        
    base_tax = 80
    tax_150 = 6
    tax_per_mwait = 3
    cancelpenalty = 80
    
    if distance == 0:
        cost = cancelpenalty + (waiting * tax_per_mwait)
        return cost
    
    add_tax = (distance // 150) * tax_150
    add_wait = waiting * tax_per_mwait
    
    cost = base_tax + add_tax + add_wait
    return cost
    
    
# D:\Ilya\Working\Bobkov\2024.11.10>python -i 2.py
# >>> taxi_tax(100, 2)
# 86
# >>> taxi_tax(1500)
# 140
# >>> taxi_tax(2560)
# 182
# >>> taxi_tax(3000, -5)
# >>>