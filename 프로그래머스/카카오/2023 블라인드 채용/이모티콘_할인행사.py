# https://school.programmers.co.kr/learn/courses/30/lessons/150368

def solution(users, emoticons):
    answer = []
    sale = [0.1, 0.2, 0.3, 0.4]
    size = len(emoticons)
    def func(users, emoticons, p):
        e = emoticons[0]
        emoticons = emoticons[1:]
        stk = []
        for s in sale:
            tmp = p.copy()
            for i, u in enumerate(users):
                n, price = u
                n = n/100
                if n<=s:
                    tmp[i]+=e*(1-s)
            
            if len(emoticons):
                res = func(users, emoticons, tmp)
                if res:
                    stk.extend(res)
            if len(emoticons)==0:
                stk.append(tmp)
        if len(emoticons)<=size-1:
            return stk
    res = func(users, emoticons, [0] * len(users))
    mile = []
    price = []
    for r in res:
        m = 0
        total = 0
        for x, u in zip(r, users):
            n, p = u
            if x >= p:
                m+=1
            else:
                total += x
        mile.append(m)
        price.append(total)
    
    best_m = max(mile)
    best_p = 0 
    for i, p in enumerate(price):
        if mile[i]==best_m:
            if best_p<p:
                best_p = p
    return [best_m, int(best_p)]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))