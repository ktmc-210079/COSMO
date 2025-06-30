x = []
y = 0b10000

for i in range(2**4):
    x.append(bin(y))
    y += 1

print(x)
