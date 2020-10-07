a = int(input('first number: '))
b = int(input('second number: '))
m = 1
for n in range(2,min(a,b)):
    if (a%n == 0) & (b%n == 0):
        m = n
print(f'{a} and {b} 的最大公约数是：{m}')
print(f'{a} and {b} 的最小公倍数是：{(a*b)//m}')