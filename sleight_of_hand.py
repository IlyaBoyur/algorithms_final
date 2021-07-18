# Solution ID: 52177009
def sleight_of_hand(keys_count,  matrix_cells, players_count=2,
                    game_digits=['1','2','3','4','5','6','7','8','9']):
    fingers_count = keys_count * players_count
    return sum(0 < matrix_cells.count(digit) <= fingers_count
                for digit in game_digits)


if __name__ == '__main__':
    print(sleight_of_hand(keys_count=int(input()),
                          matrix_cells=input()+input()+input()+input()))
