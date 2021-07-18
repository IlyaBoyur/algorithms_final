# Solution ID: 52168494
def closest_zero(street_length, street):
    zeros = [
        i for (i, e) in enumerate(street.split(' ')[:street_length])
        if e == '0'
    ]
    z_i = 0
    z_len = len(zeros)
    result = []
    for i in range(0, street_length):
        if (z_i == z_len-1):
            digit = abs(i - zeros[z_i])
        else:
            d = abs(i - zeros[z_i])
            d_next = abs(i - zeros[z_i + 1])

            digit = min(d, d_next)

            if i == zeros[z_i + 1]:
                z_i += 1
        result.append(digit)
    return(' '.join([str(i) for i in result]))


if __name__ == '__main__':
    street_length = int(input())
    street = input()
    print(closest_zero(street_length, street))
