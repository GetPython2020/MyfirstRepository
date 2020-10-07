def f(a=1,b=2,c=3):
    sum=a+b+c
    return sum
print(f())  # 6
print(f(10)) # 15
print(f(10,20)) # 33
print(f(10,20,30)) # 60