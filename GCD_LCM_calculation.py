a = int(input('first number: '))
b = int(input('second number: '))
m = 1
for n in range(2,min(a,b)):
    if (a%n == 0) & (b%n == 0):
        m = n
print(f'The greatest common divisor of {a} and {b} is：{m}')
print(f'The least common multiple of {a} and {b} is：{(a*b)//m}')
