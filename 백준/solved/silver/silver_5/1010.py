import operator as op
from functools import reduce
import sys

def nCr(n, r):
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

test = int(sys.stdin.readline())
for i in range(test):
    n,m = map(int, sys.stdin.readline().split())
    print(nCr(m,n))