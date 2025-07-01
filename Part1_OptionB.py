import Part1_PaymentGenerator as gen
from Part1_ParameterValues import *

avg = 0

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

print(avg)
input()
