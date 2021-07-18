# Solution ID: 52177445
def closest_zero(street):
    street_length = len(street)
    zeros = [index for (index, number) in enumerate(street) if number == '0']
    result = [0] * street_length
    # Before first zero
    first_zero = zeros[0]
    for number in range(first_zero):
        result[number] = first_zero - number
    # Between first and last zeros (if any)
    left_zero = first_zero
    for right_zero in zeros[1:]:
        for number in range(left_zero, right_zero):
            result[number] = min(number - left_zero, right_zero - number)
        left_zero = right_zero
    # After last zero
    last_zero = zeros[-1]
    for number in range(last_zero, street_length):
        result[number] = number - last_zero
    return result


if __name__ == '__main__':
    input()
    print(' '.join([
        str(number)
        for number in closest_zero(input().rstrip().split(' '))
    ]))
