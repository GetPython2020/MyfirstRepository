for g in range(0,101):
    for m in range(0,101):
        for x in range(0,101):
            if (g*5+m*3+x/3 == 100) & (g+m+x == 100):
                print(f'{g}只公鸡，{m}只母鸡，{x}只小鸡')

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))