# Solution ID: 52179765
def closest_zero(street, empty_pose_value='0', first_zero_index=0,
                 last_zero_index=-1):
    street_length = len(street)
    zeros = [
        index
        for (index, number) in enumerate(street)
        if number == empty_pose_value
    ]
    result = [int(empty_pose_value)] * street_length
    # Before first zero
    first_zero = zeros[first_zero_index]
    for number in range(first_zero):
        result[number] = first_zero - number
    # Between first and last zeros (if any)
    left_zero = first_zero
    for right_zero in zeros[first_zero_index+1:]:
        for number in range(left_zero, right_zero):
            result[number] = min(number - left_zero, right_zero - number)
        left_zero = right_zero
    # After last zero
    last_zero = zeros[last_zero_index]
    for number in range(last_zero, street_length):
        result[number] = number - last_zero
    return result


if __name__ == '__main__':
    input()
    print(' '.join([
        str(number)
        for number in closest_zero(street=input().rstrip().split(' '))
    ]))
