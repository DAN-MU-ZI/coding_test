# https://school.programmers.co.kr/learn/courses/30/lessons/92341#

from math import ceil
def solution(fees, records):
    answer = []
    base_time, base_charge, time, charge = fees
    
    in_di = {}
    records_di = {}
    for r in records:
        t, n, io = r.split()
        #n = int(n)
        h, m = map(int,t.split(":"))
        if io=='IN':
            in_di[n] = m+h*60
        else:
            if n in records_di.keys():
                records_di[n]+=h*60+m-in_di[n]
            else:
                records_di[n]=h*60+m-in_di[n]
            del in_di[n]
    
    for n, v in in_di.items():
        if n in records_di.keys():
            records_di[n]+=23*60+59-in_di[n]
        else:
            records_di[n]=23*60+59-in_di[n]
    
    for k, v in records_di.items():
        if records_di[k] > base_time:
            records_di[k] = base_charge + ceil((records_di[k]-base_time)/time)*charge
        else:
            records_di[k] = base_charge

    return [x[1] for x in sorted(records_di.items())]

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))