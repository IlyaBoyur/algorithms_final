# Solution ID: 52222119
def quick_sort(array, left, right):
    def partition(left, right):
        pivot = array[right]
        divider = left-1
        for current in range(left, right):
            if array[current] < pivot:
                divider += 1
                array[divider], array[current] = (array[current],
                                                  array[divider])
        array[divider + 1], array[right] = (array[right],
                                            array[divider + 1])
        return divider + 1
    if right <= left:
        return
    divider = partition(left, right)
    quick_sort(array, left, divider - 1)
    quick_sort(array, divider + 1, right)


if __name__ == '__main__':
    length = int(input())
    players = [(lambda player: (-int(player[1]),
                                int(player[2]),
                                player[0]))(input().split(' '))
               for _ in range(length)]
    quick_sort(players, 0, length-1)
    print(*[player[2] for player in players], sep='\n')