# Solution ID: 52177445
def closest_zero(street):
    street_length = len(street)
    zeros = [i for (i, e) in enumerate(street) if e == '0']
    result = [0] * street_length
    # Before first zero
    for i in range(zeros[0]):
        result[i] = zeros[0] - i
    # Between first and last zeros (if any)
    left_zero = zeros[0]
    for right_zero in zeros[1:]:
        for i in range(left_zero, right_zero):
            result[i] = min(i - left_zero, right_zero - i)
        left_zero = right_zero
    # After last zero
    for i in range(zeros[-1], street_length):
        result[i] = i - zeros[-1]
    return result


if __name__ == '__main__':
    input()
    print(' '.join([
        str(i)
        for i in closest_zero(input().rstrip().split(' '))
    ]))
