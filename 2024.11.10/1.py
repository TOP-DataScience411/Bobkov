import re

def StrPass(pas: str, /) -> bool:
    if len(pas) < 8:
        return False
    
    if not re.search(r'[A-Z]', pas):
        return False
        
    if not re.search(r'[a-z]', pas):
        return False
        
    if not re.search(r'[0-9]', pas):
        return False
        
    if not re.search(r'[!@#$%^&*()]', pas):
        return False
        
    return True
    
    
# D:\Ilya\Working\Bobkov\2024.11.10>python -i 1.py
# >>> StrPass("Password123!")
# True
# >>> StrPass("StrongPass1@")
# True
# >>> StrPass("Secure#2024")
# True
# >>> StrPass("MyP@ssw0rd!")
# True
# 
# D:\Ilya\Working\Bobkov\2024.11.10>python -i 1.py
# >>> StrPass("weakpass")
# False
# >>> StrPass("12345678")
# False
# >>> StrPass("PASSWORD")
# False
# >>> StrPass("abcde123")
# False
# >>> StrPass("!@#$%^&*()")
# False