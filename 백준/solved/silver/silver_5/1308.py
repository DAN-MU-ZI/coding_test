# D-Day

import sys
from datetime import date, timedelta

y1,m1,d1 = map(int,sys.stdin.readline().split())
y2,m2,d2 = map(int,sys.stdin.readline().split())

time_dff = date(y2,m2,d2)-date(y1,m1,d1)
after_thousands_year = date(y1+1000,m1,d1)-date(y1,m1,d1)
if time_dff>=after_thousands_year:
    print("gg")
else:
    print("D-%i"%time_dff.days)
