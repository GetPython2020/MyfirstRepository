# perfect number = sum of all numbers that can divide the perfect number  eg. 6 = 1+2+3
perfect = []

for n in range(1,10000):
    factors = []
    for i in range(1,n):
        if n%i == 0:
            factors.append(i)
    if n == sum(factors):
        perfect.append(n)
print(perfect)
