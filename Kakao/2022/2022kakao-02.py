def solution(cap, n, deliveries, pickups):

    answer = 0

    while (deliveries != [0] * n) and (pickups != [0] * n):
        c = min(cap, sum(deliveries))
        max_go = 0
        for i in range(n-1, -1, -1):
            if deliveries[i] > 0 and deliveries[i] <= c:
                c -= deliveries[i]
                deliveries[i] = 0
                max_go = max(max_go, i + 1)

            elif c < deliveries[i]:
                deliveries[i] -= c
                c = 0
                max_go = max(max_go, i + 1)

            if c == 0:
                break

        max_come = 0
        for i in range(n-1, -1, -1):
            if pickups[i] > 0 and c + pickups[i] <= cap:
                c += pickups[i]
                pickups[i] = 0
                max_come = max(max_come, i)

            elif c + pickups[i] > cap:
                c = cap
                pickups[i] -= (cap - c)
                max_come = max(max_come, i)

            if c == cap:
                break

        d = max(max_go, max_come)
        if d == 0:
            break
        answer += 2 * d

    return answer
