
perfect = []

for n in range(1,10000):
    factors = []
    for i in range(1,n):
        if n%i == 0:
            factors.append(i)
    if n == sum(factors):
        perfect.append(n)
print(perfect)
