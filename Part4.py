import Part1_PaymentGenerator as gen
from Part1_ParameterValues import *

n = list(map(int, input().split()))
#replace default value with [first value, last value, interval]

for w in range(n[0], n[1] + n[2], n[2]):
    #for each w
    avg = 0
    #reset value
    for i in gen.gen(T):
        #for each possibility
        balance = W - w - B
        channel = w
        #reset values
        for j in range(T):
            #for each payment
            balance += balance * R
            #interest
            if channel >= (int(i[-T + j]) + 1) * 5:
                #if there are enough BTC in the channel
                channel -= (int(i[-T + j]) + 1) * 5
                #off-chain payment
            else:
                #otherwise
                balance -= (int(i[-T + j]) + 1) * 5 + C
                #on-chain payment
        balance += channel - B
        #channel closure
        avg += balance

    avg = avg / 2 ** T

    print(w, avg)

input()
