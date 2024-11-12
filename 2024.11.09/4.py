def main():
    err_dict = {}
    
    while True:
        input_dl = input("Введите число и ошибку через пробел: ")
        if input_dl.strip() == "":
            break
        dict_parts = input_dl.split()
        if len(dict_parts) != 2:
            print("Введено не два значения!")
            continue
        
        num, text = dict_parts
        err_dict[text] = num
        
    search = input("Введите ошибку:")
    
    keyser = err_dict.get(search)
    
    if keyser is not None:
        print(f"Найдено: {keyser}")
    else:
        print("Ошибка: ValueError")
        
main()


# D:\Ilya\Working\Bobkov\2024.11.09>python 4.py
# Введите число и ошибку через пробел: 1004 ER_CANT_CREATE_FILE
# Введите число и ошибку через пробел: 1005 ER_CANT_CREATE_TABLE
# Введите число и ошибку через пробел: 1006 ER_CANT_CREATE_DB
# Введите число и ошибку через пробел: 1007 ER_DB_CREATE_EXISTS
# Введите число и ошибку через пробел: 1008 ER_DB_DROP_EXISTS
# Введите число и ошибку через пробел: 1010 ER_DB_DROP_RMDIR
# Введите число и ошибку через пробел: 1016 ER_CANT_OPEN_FILE
# Введите число и ошибку через пробел: 1022 ER_DUP_KEY
# Введите число и ошибку через пробел:
# Введите ошибку:ER_CANT_CREATE_DB
# Найдено: 1006
# 
# D:\Ilya\Working\Bobkov\2024.11.09>python 4.py
# Введите число и ошибку через пробел: 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# Введите число и ошибку через пробел: 4108 ER_GIPK_COLUMN_EXISTS
# Введите число и ошибку через пробел: 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
# Введите число и ошибку через пробел: 4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
# Введите число и ошибку через пробел: 4114 ER_CTE_RECURSIVE_NOT_UNION
# Введите число и ошибку через пробел:
# Введите ошибку:ER_CANT_OPEN_FILE
# Ошибка: ValueError