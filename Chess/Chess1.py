import copy
matrix = [[0 for i in range (8)]for j in range(8)]
cnt = 0
def strikeout(i, j):
  for x in range(8):
    matrix[x][j] += 1
    matrix[i][x] += 1
    if 0 <= i + j - x < 8:
      matrix[i + j - x][x] += 1
    if 0 <= i - j + x < 8:
      matrix[i - j +x][x] += 1
  matrix[i][j] = -1

def delete(i, j):
  for x in range(8):
    matrix[x][j] -= 1
    matrix[i][x] -= 1
    if 0 <= i + j - x < 8:
      matrix[i + j - x][x] -= 1
    if 0 <= i - j + x < 8:
      matrix[i - j +x][x] -= 1
  matrix[i][j] = 0

def realization(i):
    count = 0
    for j in range(8):
        if matrix[i][j] == 0:
            strikeout(i, j)
            if i == 7:
                matrix_1 = copy.deepcopy(matrix)
                for i in range (8):
                    for j in range (8):
                        if matrix_1[i][j] == -1:
                            matrix_1[i][j] = 8
                        else:
                            matrix_1[i][j] = 0
                for i in range(8):
                    print(matrix_1[i])
                    count += 1
                print()
                break
            else:
                realization(i + 1)
            delete(i, j)

realization(0)
