import sys
answer = [0, 0] # white, blue


def check_cond(paper):
    left_top = paper[0][0]
    cond = 0
    if left_top == 0:
        cond = 1
    for lst in paper:
        if cond in lst:
            return True
    return False


def cut(paper):
    length = len(paper)
    if length == 1:
        return 1
    half = (length // 2)
    fraction = [[] for _ in range(4)]
    
    for i in range(length // 2):
        top_part = paper[i]
        bottom_part = paper[i + half]
        fraction[0].append(top_part[0:half])
        fraction[1].append(top_part[half:length])
        fraction[2].append(bottom_part[0:half])
        fraction[3].append(bottom_part[half:length])
    
    for i in range(4):
        if check_cond(fraction[i]):
            cut(fraction[i])
        else:
            global answer
            color = fraction[i][0][0]
            answer[color] += 1
            
    return True
  

def solution():
    n = int(sys.stdin.readline().rstrip())
    paper = []
    global answer
    
    for _ in range(n):
        paper.append(list(map(int, sys.stdin.readline().rstrip().split())))
        
    if check_cond(paper):
        cut(paper)
    else:
        color = paper[0][0]
        answer[color] += 1
        
    for num in answer:
        print(num)
    
    
solution()