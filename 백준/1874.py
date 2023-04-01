n = int(input())

res = []
stk = []
cnt = 1
for i in range(n):
    need = int(input())
    while cnt <= need:
        stk.append(cnt)
        res.append('+')
        cnt+=1
    if stk[-1] == need:
        res.append('-')
        stk.pop()
    else:
        res = ['NO']
        break

for i in res:
    print(i)