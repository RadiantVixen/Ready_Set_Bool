


def adder(a, b):
    if a < 0 or b < 0:
        raise ValueError("adder only supports non-negative integers")

    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1

    return a





if __name__ == "__main__":
    a = 158
    b = 2
    print(f"adder(a, b) = {adder(a, b)}")
