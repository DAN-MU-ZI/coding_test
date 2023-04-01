# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    answer = [50,50,0,0]
    for i, row in enumerate(wallpaper):
        for j, r in enumerate(row):
            if r=='#':
                answer[0] = min([answer[0], i])
                answer[1] = min([answer[1], j])
                answer[2] = max([answer[2], i+1])
                answer[3] = max([answer[3], j+1])
    return answer

print(solution([".#...", "..#..", "...#."]))
print(solution(	["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution(	[".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))