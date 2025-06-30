def gen(n):
    x = []
    y = 2**n
    for i in range(2**n):
        x.append(bin(y))
        y += 1
    return x

if __name__ == "__main__":
    print(gen(int(input())))
