import sys

n = int(sys.stdin.readline())
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
    distance = (x1-x2)**2+(y1-y2)**2
    rad_diff = r1**2-2*r1*r2+r2**2
    rad_sum = r1**2+2*r1*r2+r2**2
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif distance < rad_diff:
        print(0)
    elif distance == rad_diff:
        print(1)
    elif rad_diff < distance and distance < rad_sum:
        print(2)
    elif distance == rad_sum:
        print(1)
    else:
        print(0)