from copy import deepcopy

cond_lst = ['lang', 'job', 'career', 'food', 'score']


def solution(info, query):
    answer = []
    info_lst = parse_info(info)
    query_lst = parse_query(query)

    for i in range(len(query_lst)):
        dup = deepcopy(info_lst)
        filter(dup, query_lst[i])
        answer.append(len(dup))

    return answer


def parse_info(info):
    lst = []
    for person in info:
        prop = person.split()
        lst.append({
            'lang': prop[0],
            'job': prop[1],
            'career': prop[2],
            'food': prop[3],
            'score': prop[4],
        })
    return lst


def parse_query(query):
    lst = []
    for q in query:
        prop = q.split()
        index = [1, 3, 5]
        for i in sorted(index, reverse=True):
            del prop[i]
        lst.append(prop)
    return lst


def filter(info_lst, query):
    for i in range(len(info_lst) - 1, -1, -1):
        for cond_index in range(5):
            cond = cond_lst[cond_index]
            if cond == 'score' and query[cond_index] != '-' and (int(info_lst[i][cond]) < int(query[cond_index])):
                del info_lst[i]
                break
            if cond != 'score' and query[cond_index] != '-' and info_lst[i][cond] != query[cond_index]:
                del info_lst[i]
                break
