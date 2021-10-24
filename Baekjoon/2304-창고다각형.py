import sys

def solution():
    pillars = []; roof = []; answer = 0
    N = int(input())
    for _ in range(N):
        L, H = map(int, sys.stdin.readline().rstrip().split())
        pillars.append((L, H))
    sort(pillars)
    start, _ = pillars[0]; end, _ = pillars[-1]
    for L, H in pillars:
        if is_roof(L, H, pillars):
            roof.append((L, H))
    for i in range(start, end + 1):
        answer += get_area(i, roof)
    return answer
    
def sort(pillars):
    length = len(pillars)
    for i in range(length):
        for k in range(i + 1, length):
            L_i, _ = pillars[i]; L_k, _ = pillars[k]
            if(L_i > L_k):
                (pillars[i], pillars[k]) = (pillars[k], pillars[i])
    
def is_roof(L, H, pillars):
    left = True; right = True
    for (x, y) in pillars:
        if y > H:
            if L > x:
                left = False
            else:
                right = False
        if not left and not right:
            return False
    return True

def get_area(i, roof):
    area = 0
    for (L, H) in roof:
        if L == i:
            return H
        elif L < i:
            area = H
        else:
            area = min(area, H)
            return area

print(solution())