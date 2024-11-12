def valid_email(in_email):
    if in_email.count('@') !=1:
        return None
    
    lo_part, up_part = in_email.split('@')
    
    if not lo_part:
        return None
    
    if not up_part:
        return None
    
    if not '.' in up_part or up_part.startswith('.') or up_part.endswith('.'):
        return None
    else:
        if not (up_part.endswith('.ru') or up_part.endswith('.com') or up_part.endswith('.net')):
            return None
            
    ValidChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"
    
    if lo_part.count('.') >= 1:
        return None
    
    for char in lo_part:
        if char not in ValidChars:
            return None
    
    for char in up_part:
        if char not in ValidChars:
            return None
    
    if up_part.count('.') >= 2:
        return None
        
    return True
    
def main():
    email_in = input('Введите e-mail: ')
    
    if valid_email(email_in):
        print('Корректно.')
    else:
        print('Не корректно.')
        
main()

# D:\Ilya\Working\Bobkov\2024.11.09>python -i 1.py
# Введите e-mail: googa@mama
# Не корректно.
# >>> main()
# Введите e-mail: magi@m@magi.com
# Не корректно.
# >>> main()
# Введите e-mail: magi@magi.com
# Корректно.


#  Да, я знаю, что у нас не допускаются регулярные выражения, но я все равно не удержался.
#
# import re
# 
# def valid_email(in_email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     
#     if re.match(pattern, in_email):
#         domain_part = in_email.split('@')[1]
#         if domain_part.count('.') < 1:
#             return None
#         if '..' in domain_part:
#             return None
#         if domain_part.endswith('.'):
#             return None
#         return True
#     else:
#         return None
# 
# def main():
#     email_in = input('Введите e-mail: ')
#     
#     if valid_email(email_in):
#         print('Корректно.')
#     else:
#         print('Не корректно.')
#       
#       
# main()