# Solution ID: 52177009
def sleight_of_hand(keys_count,  matrix_cells, players_count=2,
                    numbers_list=range(1, 10)):
    fingers_count = keys_count * players_count
    return sum(0 < matrix_cells.count(f'{digit}') <= fingers_count
                for digit in numbers_list)


if __name__ == '__main__':
    print(sleight_of_hand(keys_count=int(input()),
                          matrix_cells=input()+input()+input()+input()))
