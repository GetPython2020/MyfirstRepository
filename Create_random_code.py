# generate random code using numbers and letters
import random
def check(n=4):
    all_chas = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code =''
    i=1
    while i<=n:
        j=random.randint(0,len(all_chas)-1)
        code += all_chas[j]
        i+=1
    return code

if __name__ == '__main__':
    print(check(6))

