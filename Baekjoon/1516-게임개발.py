#
# Baekjoon 1516 - 게임 개발
# Gold 3
# 그래프 이론
#

import sys
input = sys.stdin.readline


N = int(input())
built = [-1] * (N+1)
building = {}
for i in range(1, N + 1):
    info = list(map(int, input().split()))[:-1]
    t, pre_build = info[0], info[1:]
    building[i] = {'takes': t, 'pre_build': pre_build}

while -1 in built[1:]:
    for i in range(1, N+1):
        b = building[i]
        # 선수 건물이 없으면 Build it
        if len(b['pre_build']) == 0:
            built[i] = b['takes']
        # 선수 건물이 있으면
        else:
            can_build = True
            pre_t = []
            for pre in b['pre_build']:
                if built[pre] == -1:
                    can_build = False
                    break
                else:
                    pre_t.append(built[pre])

            if can_build:
                built[i] = max(pre_t) + b['takes']

for time in built[1:]:
    print(time)
