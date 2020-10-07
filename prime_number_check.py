n = int(input('enter your number: '))
sum = 0
for m in range(2,n):
    sum += (n%m == 0)
if sum >0:
    print(f'{n} is not a prime number')
else:
    print(f'{n} is a prime number')