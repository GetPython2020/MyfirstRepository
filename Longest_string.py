s='abcfbc'
m = len(s)
out=''
for i in range(0, m):
    for j in range(i + 1, m):
        for t in range(0, j):
            if s[j] != s[t]:
                out[i] += s[j]
print(out)
