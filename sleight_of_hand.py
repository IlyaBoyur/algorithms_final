MATRIX_ROW_COUNT = 4


# Solution ID: 52166771
def sleight_of_hand(keys_count, matrix_cells):
    digit_counts = [0] * 10
    for char in matrix_cells:
        if char.isdigit():
            digit_counts[int(char)] += 1
    return(len([digit for digit in digit_counts if 0 < digit <= (keys_count * 2)]))


if __name__ == '__main__':
    keys_count = int(input())
    matrix_cells = []
    for i in range(MATRIX_ROW_COUNT):
        matrix_cells.append(input().rstrip())
    print(sleight_of_hand(keys_count, ''.join(matrix_cells)))
