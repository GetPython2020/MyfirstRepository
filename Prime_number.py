# Prime number within 100, not include 1

for i in range(2,101):
    p = True
    for j in range(2,i-1):
        if i%j == 0:
            p = False
            break
        else:
            continue
    if p == True:
        print(f'{i} is a prime number')   
