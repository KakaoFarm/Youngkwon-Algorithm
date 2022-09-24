def is_later(date, today):
    a, b, c = map(int, date.split('.'))
    d, e, f = map(int, today.split('.'))

    if a > d:
        return True
    elif a < d:
        return False
    else:
        if b > e:
            return True
        elif b < e:
            return False
        else:
            if c > f:
                return True
            else:
                return False


def get_2digit(num):
    n = int(num)
    if n < 10:
        return "0" + str(n)
    else:
        return str(n)


def add_month(date, m):
    a, b, c = map(int, date.split('.'))
    b += m
    if b > 12:
        if b % 12 != 0:
            a += b // 12
            b %= 12
        else:
            a += (b // 12) - 1
            b = 12
    return get_2digit(a) + "." + get_2digit(b) + "." + get_2digit(c)


def solution(today, terms, privacies):
    T = {}
    for t in terms:
        (k, v) = t.split()
        T[k] = int(v)

    answer = []
    for i in range(len(privacies)):
        p = privacies[i]
        date, t = p.split()
        due = add_month(date, T[t])
        if not is_later(due, today):
            answer.append(i+1)

    return answer
