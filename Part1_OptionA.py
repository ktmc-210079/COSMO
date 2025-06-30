import Part1_PaymentGenerator as gen
from Part1_ParameterValues import *

avg = 0

for i in gen.gen(T):
    #for each possibility
    balance = W
    #reset value
    for j in range(T):
        #for each payment
        balance += balance * R
        #interest
        balance -= (int(i[-T + j]) + 1) * 5 + C
        #payment
    avg += balance

avg = avg / 2 ** T

print(avg)
