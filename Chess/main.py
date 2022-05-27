from random import randint

# Вывод матрицы
def Print(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("\n")

# Исключение ячеек, перекрытых ферзем
def strikeout(matrix, row, col):
    for j in range(8):
        if matrix[row][j] != -1:
            matrix[row][j] = 1

        if j == col:
            if matrix[row][j] != -1 and matrix[row][j] != 1:
                matrix[row][j] = 1


    # Первая диагональ
    a = 0 if row - col < 0 else row - col
    b = 0 if col - row < 0 else col - row

    #print("Начальная точка 1 диагонали", a, b, "\n")

    while a < 8 and b < 8:
        if matrix[a][b] != 1 and matrix[a][b] != -1:
            matrix[a][b] = 1
        a += 1
        b += 1

    # Вторая диагональ
    a = 7 if col + row > 7 else col + row
    b = col - (a - row)

    #print("Начальная точка 2 диагонали", a, b, "\n")

    while a > -1 and b < 8:
        if matrix[a][b] != 1 and matrix[a][b] != -1:
            matrix[a][b] = 1
        a -= 1
        b += 1

#Подсчет значений
def Count(matrix, n, row):
    for j in range(n):
        if matrix[row][j] != 1 and matrix[row][j]!= -1 :
            k = 0
            for f in range(n):
                if matrix[row][f] != 1 and matrix[row][f] != -1:
                    k += 1

            for f in range(n):
                if matrix[f][j] != 1 and matrix[f][j]!= -1:
                    k += 1

            a = 0 if row - j < 0 else row - j
            b = 0 if j - row < 0 else j - row
            while a < 8 and b < 8:
                if matrix[a][b] != 1  and matrix[a][b]!= -1:
                    k += 1
                a += 1
                b += 1

            a = 7 if j + row > 7 else j + row
            b = j - (a - row)
            while a > -1 and b < 8:
                if matrix[a][b] != 1 and matrix[a][b]!= -1:
                    k += 1
                a -= 1
                b += 1
            matrix[row][j] = k-4

#Поиск наименьших
def min(matrix, n, row):
    k = 1000
    for j in range(n):
        if matrix[row][j] < k and matrix[row][j] != 1 and matrix[row][j] != -1:
            k = matrix[row][j]
    return k

# Создание матрицы
n = 8
matrix = [[0 for j in range(n)] for i in range(n)]
print("Начальная матрица")
Print(matrix)

col = 0
# Размещение ферзя
matrix[0][0] = -1
print("Размещение ферзя")
Print(matrix)

for row in range(n - 1):

    # Вычеркивание линий
    strikeout(matrix, row, col)
    # Print(matrix)

    # Подсчет значений
    Count(matrix, n, row + 1)
    # Print(matrix)

    a = min(matrix, n, row + 1)
    # print("Наименьшее число",a, "\n")

    for j in range(n):
        if matrix[row + 1][j] == a:
            col = j
            break
    # print("Индекс",row+1,col, "\n")
    matrix[row + 1][col] = -1




for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            matrix[i][j] = 0
        if matrix[i][j] == -1:
            matrix[i][j] = 8

Print(matrix)