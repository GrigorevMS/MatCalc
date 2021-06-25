def inputmas(n):
    answer = []
    for i in range(n):
        s = input()
        answer.append(list(s.split()))
    return(answer)
'''------------------------------------------------------------------------------------------'''
def output(mas, sch):
    s = "                " * sch
    for i in range(len(mas)):
        print(s, end = "")
        for j in range(len(mas[i])):
            print(mas[i][j], end = " ")
        if i != len(mas[i]) - 1:
            print()
'''------------------------------------------------------------------------------------------'''
def StrToInt(n, mas):
    for i in range(n):
        for j in range(n):
            mas[i][j] = int(mas[i][j])
    return(mas)
'''------------------------------------------------------------------------------------------'''
def eraser(n, x, mas):
    answer = []
    sch = -1
    for i in range(1, n):
        answer.append([])
        sch += 1
        for j in range(n):
            if j != x:
                answer[sch].append(mas[i][j])
    return(answer)
'''------------------------------------------------------------------------------------------'''
def determinant_2x2(mas):
    return(mas[0][0] * mas[1][1] - mas[0][1] * mas[1][0])
'''------------------------------------------------------------------------------------------'''
def determinant(n, mas, sch):
    if n == 2:
        det = determinant_2x2(mas)
    else:
        det = 0
        for i in range(n):
            masal = eraser(n, i, mas)
            extra = pow(-1, i) * mas[0][i] * determinant(n - 1, masal, sch + 1)
            output(masal, sch)
            print(" =", extra, '\n')
            det += extra
    return(det)
'''------------------------------------------------------------------------------------------'''
print("Введите степень матрицы: ")
n = int(input())
print("Введите матрицу степени n: ")
mas = StrToInt(n, inputmas(n))
print()
sch = 0
print("Определитель заданной матрицы =", determinant(n, mas, sch))
