from typing import Tuple
from statistics import mean, median, mode, StatisticsError
from math import prod

def math_fq(num1: float, num2: float, *args: float) -> Tuple[float, float, float, float, str]:
     # docstring
     """Вычисляет основные меры центральной тенденции: среднее арифметическое,
    медиану, геометрическое и гармоническое средние.
    
    Args:
        num1 (float): Первое число.
        num2 (float): Второе число.
        *args (float): Произвольное количество вещественных чисел.
        
    Returns:
        Tuple[float, float, float, float, str]: Среднее арифметическое,
        медиана, геометрическое среднее, гармоническое среднее и мода или сообщение об ошибке.
    P.S. Знаю, что мода не входила в задание, я решил её включить по собственному желанию.
    """
     numbers = [num1, num2] + list(args)
     
     n = len(numbers)
     gem = prod(numbers) ** (1/n)
     har = n / sum(1/x for x in numbers)
     avg = mean(numbers)
     med = median(numbers)
     
     if len(set(numbers)) == len(numbers):
         mod = "Мода не определена."
     else:
         mod = mode(numbers)
         
         
     print(f"Median: {med} | Ariphmetic: {avg} | Geometric: {gem} | Harmony: {har} | Moda {mod}")
     return avg, med, gem, har, mod
     
# D:\Ilya\Working\Bobkov\2024.11.10>python -i 5.py
# >>> math_fq(1, 2, 3, 4)
# Median: 2.5 | Ariphmetic: 2.5 | Geometric: 2.213363839400643 | Harmony: 1.92 | Moda Мода не определена.
# (2.5, 2.5, 2.213363839400643, 1.92, 'Мода не определена.')
# >>> math_fq(1, 2, 3, 7)
# Median: 2.5 | Ariphmetic: 3.25 | Geometric: 2.5457298950218306 | Harmony: 2.0240963855421685 | Moda Мода не определена.
# (3.25, 2.5, 2.5457298950218306, 2.0240963855421685, 'Мода не определена.')
# >>> math_fq(1, 2, 1, 7)
# Median: 1.5 | Ariphmetic: 2.75 | Geometric: 1.9343364202676694 | Harmony: 1.5135135135135136 | Moda 1
# (2.75, 1.5, 1.9343364202676694, 1.5135135135135136, 1)