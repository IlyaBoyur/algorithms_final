import sys


MATRIX_SIZE = (4+1)*4


# Solution ID: 52166771
def sleight_of_hand():
    k_x2 = int(input()) * 2
    digit_counts = [0] * 10
    matrix_cells = sys.stdin.read(MATRIX_SIZE)
    for ch in matrix_cells:
        if ch.isdigit():
            digit_counts[int(ch)] += 1
    print(len([num for num in digit_counts if 0 < num <= k_x2]))


# Solution ID: 52168494
def closest_zero():
    n = int(input())
    zeros = [
        i for (i, e) in enumerate(sys.stdin.readline().rstrip().split(' ')[:n])
        if e == '0'
    ]
    z_i = 0
    z_len = len(zeros)
    result = []
    for i in range(0, n):
        if (z_i == z_len-1):
            digit = abs(i - zeros[z_i])
        else:
            d = abs(i - zeros[z_i])
            d_next = abs(i - zeros[z_i + 1])

            if d < d_next:
                digit = d
            else:
                digit = d_next

            if i == zeros[z_i + 1]:
                z_i += 1
        result.append(digit)
    print(' '.join([str(i) for i in result]))


def main():
    closest_zero()
    sleight_of_hand()


if __name__ == '__main__':
    main()
