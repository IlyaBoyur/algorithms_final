# Solution ID: 52177445
def closest_zero(street):
    street_length = len(street)
    zeros = [i for (i, e) in enumerate(street) if e == '0']
    result = [0] * street_length
    # Before first zero
    for i in range(zeros[0]):
        result[i] = zeros[0] - i
    # # Between first and last zeros (if any)
    first_zero = zeros[0]
    for zero in zeros[1:]:
        for i in range(first_zero, zero):
            result[i] = min(i - first_zero, zero - i)
        first_zero = zero
    # After last zero
    for i in range(zeros[-1], street_length):
        result[i] = i - zeros[-1]
    return(' '.join([str(i) for i in result]))


if __name__ == '__main__':
    input()
    street = input()
    print(closest_zero(street.rstrip().split(' ')))
