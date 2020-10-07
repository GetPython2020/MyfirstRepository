def addTwoNumbers(l1, l2):
    m = len(l1)
    num1=0
    num2=0
    for i in range(0, m):
        num1 += l1[i] * (10 ** i)
    n = len(l2)
    for j in range(0, n):
        num2 += l2[j] * (10 ** j)
    sum = num1 + num2
    output = []

    while sum > 0:
        output.append(sum % 10)
        sum = sum // 10
    print(num1)
    print(num2)
    print(output)


addTwoNumbers([2,3,4],[1,3,6])
