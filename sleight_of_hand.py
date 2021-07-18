# Solution ID: 52177009
def sleight_of_hand(keys_count, matrix_cells):
    k_x2 = keys_count * 2
    return sum([0 < matrix_cells.count(f'{digit}') <= k_x2
                for digit in range(10)])


if __name__ == '__main__':
    print(sleight_of_hand(keys_count=int(input()),
                          matrix_cells=input()+input()+input()+input()))
