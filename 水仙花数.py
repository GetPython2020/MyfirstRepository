for n in range(100,1000):
    h = n//100
    t = (n-h*100)//10
    o = n-h*100-t*10
    if h**3+t**3+o**3 == n:
        print(f'{n} is a 水仙花数')

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)