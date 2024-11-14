def convert(value: str, ins: int, ino: int) -> str:
    # docstring
    """Конвертирует число из одной системы счисления в другую.
    
    Args:
        value (str): Число в строковом формате.
        ins (int): Основание исходной системы счисления.
        ino (int): Основание целевой системы счисления.
        
    Returns:
        str: Число в целевой системе счисления.
    """
    if ins < 2 or ins > 36 or ino < 2 or ino > 36:
        raise ValueError("Основание должно быть в диапазоне от 2 до 36.")
    
    try:
        decimal_value = int(value, ins)
    except ValueError:
        return "Ошибка: Неверное значение для данной системы счисления."
    except TypeError:
        return "Int Объект не может быть конвертирован из non-string. Ваше число должно быть заключено в двойные или одиночные кавычки."
    
    if ino == 10:
        return str(decimal_value)
        
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while decimal_value > 0:
        result = digits[decimal_value % ino] + result
        decimal_value //= ino
    
    return result if result else 0
    
# ПРИМЕЧАНИЕ: Я один раз нарушил логику подсчета не потому, что была нарушена в вычислениях, а как именно я собирал данные и в итоге все, кроме 1 у меня терялись, но я исправил ситуацию.
#
# D:\Ilya\Working\Bobkov\2024.11.10>python -i 7.py
# >>> convert("10", 10, 2)
# '1010'
# >>> convert(1101010, 2, 30)
# 'Int Объект не может быть конвертирован из non-string. Ваше число должно быть заключено в двойные кавычки.'
# >>> convert("1101010", 2, 30)
# '3G'
# >>> convert("1010111010", 2, 30)
# 'N8'
# >>> convert("Exit", 36, 2)
# '10101010000100110101'