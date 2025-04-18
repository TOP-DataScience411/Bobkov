def  dk():
    types = ['червы','бубны','пики','трефы']
    for itype in types:
        for rank in range(2, 15):
            yield (rank, itype)
            
# >>> list(dk())[::13]
# [(2, 'червы'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
# >>> list(dk())[::12]
# [(2, 'червы'), (14, 'червы'), (13, 'бубны'), (12, 'пики'), (11, 'трефы')]
# >>> list(dk())[2:5]
# [(4, 'червы'), (5, 'червы'), (6, 'червы')]
# >>> list(dk())[::5]
# [(2, 'червы'), (7, 'червы'), (12, 'червы'), (4, 'бубны'), (9, 'бубны'), (14, 'бубны'), (6, 'пики'), (11, 'пики'), (3, 'трефы'), (8, 'трефы'), (13, 'трефы')]