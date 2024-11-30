def tree_l(tree):
    count = 0
    for leaf in tree:
        if isinstance(leaf, list):
            count += tree_l(leaf)
        elif leaf == 'leaf':
            count += 1
        else:
            count += 0
    return count
 
# E:\Ilya\Working\Bobkov\2024.11.24>python -i 3.py
# >>> tree = [['leaf', 'leaf'],'leaf', [['leaf', 'leaf'], 'leaf'], 'leaf', 'leaf']
# >>> tree_l(tree)
# 8