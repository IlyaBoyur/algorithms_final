# Sollution ID: 52222128
def binary_search(array, target, left, right):
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    if left == right:
        return -1
    # # left normal part
    if array[0] < array[mid]:
        if target >= array[0]:
            if target > array[mid]:
                return binary_search(array, target, mid+1, right)
            return binary_search(array, target, left, mid)
        return binary_search(array, target, mid+1, right)
    # left broken part
    if target < array[0]:
        if target < array[mid]:
            return binary_search(array, target, left, mid)
        return binary_search(array, target, mid+1, right)
    return binary_search(array, target, left, mid)


def broken_search(array, target):
    return binary_search(array, target, 0, len(array)-1)


if __name__ == '__main__':
    input()
    target = int(input())
    print(broken_search(array=[int(number) for number in input().split(' ')],
                        target=target))
