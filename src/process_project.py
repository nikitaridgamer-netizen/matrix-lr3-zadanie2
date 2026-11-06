def process_project(matritsa, k):
    try:
        for stroka in matritsa:
            stroka.pop(k - 1)
        return matritsa
    except IndexError:
        print("Ошибка взаимодействия: передан неверный индекс столбца.")
        return matritsa
