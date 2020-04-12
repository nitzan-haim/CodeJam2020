# CodeJam 2020 Qualification Round
# Nitzan Haim April 4, 2020

def find_trace(n, mat):
    trace = 0
    for j in range(n):
        trace += mat[j][j]
    return trace


def find_row_repeats(mat):
    row_repeats = 0

    for row in mat:
        values_set = set()
        for val in row:
            if val in values_set:
                row_repeats += 1
                break
            else:
                values_set.add(val)
    return row_repeats


output = ""
test_cases = int(input())
for t in range(test_cases):
    n = int(input())  # size of matrix
    matrix = []
    for i in range(n):
        line = input()
        matrix.append(list(map(int, line.split())))

    matrix_transposed = [[row[i] for row in matrix] for i in range(n)]

    output += "Case #" + str(t+1) + ": " + \
              str(find_trace(n, matrix)) + " " + \
              str(find_row_repeats(matrix)) + " " +\
              str(find_row_repeats(matrix_transposed)) + "\n"

print(output)
