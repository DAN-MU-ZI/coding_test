import sys
from itertools import combinations

def main():
    n, k = map(int, sys.stdin.readline().split())
    base = set('antic')

    # other_alpha_count = {chr(k):0 for k in range(97,+26) if k not in base}
    other_alpha_count = set([])

    words=[]
    
    for i in range(n):
        word = set(sys.stdin.readline()[4:-5])
        
        if len(word) <= k:
            other_alpha_count.update(word)
            words.append(word)

    other_alpha_count = other_alpha_count-base

    if k<5:
        return 0
    elif k==26:
        return n
    elif len(other_alpha_count)<=k-5:
        return len(other_alpha_count)
    else:
        answer=0
        
        for group in combinations(other_alpha_count,k-len(base)):
            cnt = 0
            for word in words:
                if len(word-set(group)-base)==0:
                    cnt+=1

            if answer<cnt:
                answer=cnt

        return answer
print(main())