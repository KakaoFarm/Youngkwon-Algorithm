from itertools import combinations

def solution(orders, course):
  comb = {}
  tbl = {}
  max_val = {}
  for c in course:
    comb[c] = []
    for o in orders:
      comb[c].append(combinations(''.join(sorted(o)), c))
  
  for c in course:
    for case in comb[c]:
      for e in case:
        e = ''.join(e)
        if e not in tbl:
          tbl[e] = 1
        else:
          tbl[e] += 1
  
  answer = []
  keys = tbl.keys()
  for key in keys:
    if len(key) not in max_val:
      max_val[len(key)] = tbl[key]
    else:
      max_val[len(key)] = max(max_val[len(key)], tbl[key])
  for key in keys:
    if tbl[key] > 1 and len(key) in course and tbl[key] == max_val[len(key)]:
      answer.append(key)
  return sorted(answer)