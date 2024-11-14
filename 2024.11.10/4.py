from typing import Tuple

def count_st(cout: int, form_cout: Tuple[str, str, str]) -> str:
    #docstring
    """Возвращает существительное в зависимости от числа.
    
    Args:
        cout (int): Число для согласования.
        form_cout (Tuple[str, str, str]): Кортеж с тремя формами существительного.
        
    Returns:
        str: Согласованное существительное с числом.
    """
    if cout % 10 == 1 and cout % 100 != 11:
        return f"{cout} {form_cout[0]}"
    elif cout % 10 in (2, 3, 4) and not cout % 100 in (12, 13, 14):
        return f"{cout} {form_cout[1]}"
    else:
        return f"{cout} {form_cout[2]}"

# D:\Ilya\Working\Bobkov\2024.11.10>python -i 4.py
# >>> count_st(10, ("год", "года", "лет"))
# '10 лет'
# >>> count_st(11, ("год", "года", "лет"))
# '11 лет'
# >>> count_st(151, ("год", "года", "лет"))
# '151 год'
# >>> count_st(24, ("год", "года", "лет"))
# '24 года'