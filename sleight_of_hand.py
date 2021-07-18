# Solution ID: 52177009
MATRIX_ROW_COUNT = 4


def sleight_of_hand(keys_count, matrix_cells):
    k_x2 = keys_count * 2
    return sum([0 < matrix_cells.count(f'{digit}') <= k_x2
                for digit in range(10)])


if __name__ == '__main__':
    keys_count = int(input())
    matrix_cells = [''] * MATRIX_ROW_COUNT
    for i in range(MATRIX_ROW_COUNT):
        matrix_cells[i] = input().rstrip()
    print(sleight_of_hand(keys_count, ''.join(matrix_cells)))
