def input_project():
    while True:
        try:
            n = int(input("Введите количество строк: "))
            m = int(input("Введите количество столбцов: "))

            if n <= 0 or m <= 0:
                print("Количество строк и столбцов должно быть больше нуля")
            else:
                break

        except ValueError:
            print("Введите целые числа")

    matritsa = []

    for i in range(n):
        stroka = []
        for j in range(m):
            while True:
                try:
                    a = float(input("Введите элемент: "))
                    stroka.append(a)
                    break
                except ValueError:
                    print("Введите число")

        matritsa.append(stroka)

    while True:
        try:
            k = int(input("Введите номер столбца для удаления: "))

            if k < 1 or k > m:
                print("Такого столбца нет")
            else:
                break

        except ValueError:
            print("Введите целое число")

    return matritsa, k
