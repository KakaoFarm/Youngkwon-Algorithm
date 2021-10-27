import ast


def solution(s):
    s = s.replace('{', '[')
    s = s.replace('}', ']')
    arr = ast.literal_eval(s)
    arr = sorted(arr, key=lambda x: len(x))

    answer = []
    for lst in arr:
        for e in lst:
            if e not in answer:
                answer.append(e)
    return answer
