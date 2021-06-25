f = open('output.txt', 'w')
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
        f.write(s)
        for j in range(len(mas[i])):
            f.write(str(mas[i][j]) + " ")
        if i != len(mas[i]) - 1:
            f.write('\n')
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
            f.write(" * " + str(mas[0][i]) + " = " + str(extra) + '\n' + '\n')
            det += extra
    return(det)
'''------------------------------------------------------------------------------------------'''
print("Введите степень матрицы: ")
n = int(input())
print("Введите матрицу степени n: ")
mas = StrToInt(n, inputmas(n))
print()
sch = 0
f.write("Определитель заданной матрицы" + '\n')
output(mas, 0)
f.write('\n' + '\n')
det = determinant(n, mas, sch)
f.write("Определитель =  " + str(det))
f.close()
