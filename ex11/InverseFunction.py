MAX = 2**32 - 1

def map(x, y):
    n = (x << 16) | y
    return n / MAX


def reverse_map(f):
    n = int(f * MAX)

    x = n >> 16
    y = n & 0xFFFF

    return x, y


if __name__ == "__main__":
    f = map(1, 7)
    print(f)

    print(reverse_map(f))