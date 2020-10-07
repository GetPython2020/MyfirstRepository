#100以内的素数，不包括1
for i in range(2,101):
    p = True
    for j in range(2,i-1):
        if i%j == 0:
            p = False
            break
        else:
            continue
    if p == True:
        print(f'{i} 是一个素数')   