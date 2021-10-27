import ast


def solution(s):
    arr = s.replace('{', '[')
    arr = arr.replace('}', ']')
    arr = ast.literal_eval(arr)
    arr = sorted(arr, key=lambda x: len(x))

    answer = []
    for lst in arr:
        for e in lst:
            if e not in answer:
                answer.append(e)
    return answer
