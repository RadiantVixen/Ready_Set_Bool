


def multiplier(a, b):
    if a < 0 or b < 0:
        raise ValueError("multiplier only supports non-negative integers")

    while b != 0 
        carry = a & b
        a = a ^ b
        b = carry << 1
        print(f"carry: {carry}, a: {a}, b: {b}")

    return a





if __name__ == "__main__":
    a = 7
    b = 4
    print(f"adder(a, b) = {adder(a, b)}")
