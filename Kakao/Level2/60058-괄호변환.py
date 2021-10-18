def solution(p):
  answer = main(p)
  return answer
    
def main(p):
  if p == '':
    return ''
  (u, v) = get_uv(p)
  if is_right(u):
    return u + main(v)
  return "(" + main(v) + ")" + toggle(u[1:-1])

def get_uv(p):
  paren = [0, 0]
  u = ""
  for char in p:
    u += char
    if char == "(":
      paren[0] += 1
    else:
      paren[1] += 1
    if paren[0] == paren[1] and 0 not in paren:
      return (u, p[len(u):]) # (u, v)

def is_right(p):
  count = 0
  for char in p:
    if char == "(":
      count += 1
    else:
      count -= 1
    if count < 0:
      return False  
  return True

def toggle(p):
  result = ""
  for char in p:
    if char == "(":
      result += ")"
    else:
      result += "("
  return result