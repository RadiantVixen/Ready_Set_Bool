def map(x, y):
    n=(x<<16)+y
    return n

def reverse_map(n):
    x=n>>16
    y=n&0xFFFF
    return x, y

def print_bits(n):
    bits = f"{n:032b}"
    print(bits[:16], bits[16:])

if __name__ == "__main__":
    print(map(1, 2))
    x, y = reverse_map(map(1, 7))
    print(x, y)
    print(reverse_map(map(x, y)))
