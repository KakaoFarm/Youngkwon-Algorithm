from itertools import combinations


def solution(relation):
    key_lst = []
    noc = len(relation[0])
    ind_lst = list(range(noc))
    comb_lst = []
    for i in range(1, noc + 1):
        comb_lst = comb_lst + list(combinations(ind_lst, i))

    for comb in comb_lst:
        comb = list(comb)
        if is_key(relation, comb) and is_min(key_lst, set(comb)):
            key_lst.append(set(comb))

    answer = len(key_lst)
    return answer


def is_key(relation, ind_lst):
    storage = []
    for row in relation:
        elem = []
        for ind in ind_lst:
            elem.append(row[ind])
        if elem in storage:
            return False
        storage.append(elem)
    return True


def is_min(key_lst, com_set):
    for key_set in key_lst:
        if key_set <= com_set:
            return False
    return True
