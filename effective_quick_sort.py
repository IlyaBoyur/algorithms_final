# Solution ID: 52222119
def quick_sort(array, left, right, reverse=False):
    def partition(left, right, reverse=False):
        pivot = array[right]
        partition_index = left-1
        for index in range(left, right):
            if array[index] < pivot:
                partition_index += 1
                array[partition_index], array[index] = (array[index],
                                                        array[partition_index])
        array[partition_index + 1], array[right] = (array[right],
                                                    array[partition_index + 1])
        return partition_index + 1
    if right <= left:
        return
    partition_index = partition(left, right, reverse)
    quick_sort(array, left, partition_index - 1, reverse)
    quick_sort(array, partition_index + 1, right, reverse)


if __name__ == '__main__':
    length = int(input())
    players = [(lambda player: (-int(player[1]),
                                int(player[2]),
                                player[0]))(input().split(' '))
               for _ in range(length)]
    quick_sort(players, 0, length-1)
    print(*[player[2] for player in players], sep='\n')
