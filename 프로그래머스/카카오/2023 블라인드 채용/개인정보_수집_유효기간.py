# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    terms_dict = {x.split()[0]:int(x.split()[-1]) for x in terms}
    t_yy, t_mm, t_dd = [int(x) for x in today.split('.')]
    today_date = (t_yy*12+t_mm)*28+t_dd
    
    for i, priv in enumerate(privacies):
        date, term = priv.split()
        yy,mm,dd = map(int, date.split('.'))
        y_diff = t_yy - yy
        m_diff = t_mm - mm + y_diff * 12
        d_diff = t_dd - dd + m_diff * 28
        priv_date = (yy*12+mm)*28+dd

        if terms_dict[term]*28 <= today_date-priv_date:
            answer.append(i+1)
        
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))