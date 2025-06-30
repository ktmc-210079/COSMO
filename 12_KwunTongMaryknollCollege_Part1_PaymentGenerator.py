#generate a list of binary numbers in the format '0b10000', where the digits after the '1' indicate 5 BTC (0) or 10 BTC (10)

def gen(n):
    x = []
    y = 2**n
    for i in range(2**n):
        x.append(bin(y))
        y += 1
    return x

if __name__ == "__main__":
    print(gen(int(input())))
