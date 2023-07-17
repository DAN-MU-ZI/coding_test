import sys

length = int(sys.stdin.readline())

print(sum(list(map(int, format(length,'b')))))