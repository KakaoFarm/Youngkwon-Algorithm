PRIORITY = [
    ['*', '-', '+'],
    ['*', '+', '-'],
    ['-', '*', '+'],
    ['-', '+', '*'],
    ['+', '-', '*'],
    ['+', '*', '-']
]


def get_value(lst, i):
    origin = i
    (var1, var2) = (0, 0)
    while(True):
        i -= 1
        var1 = lst[i]
        if(var1 != '-1'):
            i = origin
            break
    while(True):
        i += 1
        var2 = lst[i]
        if(var2 != '-1'):
            i = origin
            break
    if lst[i] == '*':
        return int(var1) * int(var2)
    if lst[i] == '-':
        return int(var1) - int(var2)
    if lst[i] == '+':
        return int(var1) + int(var2)


def solution(expression):
    answer = 0
    str_stack = ""
    lst = []
    for char in expression:
        if char in ['*', '-', '+']:
            lst.append(str_stack)
            lst.append(char)
            str_stack = ""
        else:
            str_stack += char
    lst.append(str_stack)

    dup = lst[:]
    for prior in PRIORITY:
        for oper in prior:
            i = 0
            while(i < len(lst)):
                token = lst[i]
                if token == oper:
                    lst[i] = get_value(lst, i)
                    del lst[i+1]
                    del lst[i-1]
                    i -= 1
                i += 1
        answer = max(answer, abs(lst[0]))
        lst = dup[:]
    return answer
