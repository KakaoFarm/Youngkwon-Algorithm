# 
# Baekjoon 1043 - 거짓말
# Gold 4 
# 그래프 이론 (DFS)
# 

import sys


def solution():
    (num_of_people, num_of_party) = map(int, sys.stdin.readline().rstrip().split())
    truth_people = list(map(int, sys.stdin.readline().rstrip().split()))
    
    graph = [[False for _ in range(num_of_people)] for _ in range(num_of_people)]
    visited = [False for _ in range(num_of_people)]
    
    parties = []
    for _ in range(num_of_party):
        party = list(map(int, sys.stdin.readline().rstrip().split()))
        parties.append(party[1:])
        
        # 파티에 참석한 인원이 1명인 경우, edge를 생성하지 않음
        if party[0] == 1:
            continue
        
        for i in range(1, len(party)):
            for j in range(i + 1, len(party)):
                person_a = party[i]
                person_b = party[j]
                graph[person_a - 1][person_b - 1] = True
                graph[person_b - 1][person_a - 1] = True
    
    # 진실을 아는 사람이 없음
    if truth_people[0] == 0:
        return num_of_party
    truth_people = truth_people[1:]
    
    # 진실을 아는 사람에 대해서 DFS 우선 수행
    for truth in truth_people:
        dfs(truth - 1, graph, visited)
    
    # 전체를 대상으로 DFS 수행
    answer = 0
    for party in parties:
        answer_flag = True
        for person in party:
            if visited[person - 1] == True:
                answer_flag = False
                break
        if answer_flag:
            answer += 1
            
    return answer


def dfs(node, graph, visited):
    if visited[node] == True:
        return False
    visited[node] = True
    for i in range(len(graph[node])):
        if graph[node][i] == True:
            dfs(i, graph, visited)
    return True


print(solution())