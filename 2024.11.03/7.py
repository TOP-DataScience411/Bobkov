import string

def gen_remove(text):
    remove_chars = ".,:;!?–—\'\"()*/"
    return ''.join(char for char in text if char not in remove_chars)

def main():
    text = input("Введите текст: ")
    
    generated_text = gen_remove(text)
    
    print(generated_text)
    
main()

# D:\Ilya\Working\Bobkov\2024.11.03>python 7.py
# Введите текст: Доло%й зна,ки пункт.уации
# Доло%й знаки пунктуации