def filter_matrix(n):
    m = [[0 for x in range(7)] for y in range(7)]
    c, i = 7, 0

    while n != 0:
        t = 0
        while n >= c:
            t += 1
            n -= c
        m[i][n] = 1
        i += 1
        n = t

    return m


def checker(matrix):
    if matrix[0][5] and matrix[1][1] and matrix[2][6] and matrix[3][3] and matrix[4][3] and matrix[5][6] and matrix[6][2]:
        return True
    return False

m = [[0 for x in range(7)] for y in range(7)]
m[0][5] = 1
m[1][1] = 1
m[2][6] = 1
m[3][3] = 1
m[4][3] = 1
m[5][6] = 1
m[6][2] = 1
print(checker(m))

mtr = filter_matrix(1)
counter = 1
while not checker(mtr):
    print(f'Итерация {counter}')
    counter += 1
    mtr = filter_matrix(counter)

for i in mtr:
    print(*i)

print(counter)
