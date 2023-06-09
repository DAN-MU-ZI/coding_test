"""
별 찍기 - 7

문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
"""

import sys
n = int(sys.stdin.readline())
for i in range(n):
    print(' '*(n-1-i)+'*'*(2*i+1))
for i in range(n-1):
    print(' '*(i+1)+'*'*(2*(n-i-1)-1))