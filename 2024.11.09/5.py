from Scores import scores_letters

def calculate_score(word):
    score = 0
    for let_s in word.upper():
        for points, letters in scores_letters.items():
            if let_s in letters:
                score += points
                break
                
    return score
    
def main():
    word = input("Введите слово: ").strip()
    
    if not word:
        print("Ошибка, пусто.")
        return
    
    score = calculate_score(word)
    
    print(f"Количество очков за слово '{word}': {score}")
    
main()

# D:\Ilya\Working\Bobkov\2024.11.09>python 5.py
# Введите слово: Ёжидзе
# Количество очков за слово 'Ёжидзе': 15