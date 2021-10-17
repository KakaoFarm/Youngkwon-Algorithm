def solution(s):
    answer = len(s)
    for size in range(1, len(s)):
      compressed_length = compression(s, size)
      if(compressed_length < answer):
        answer = compressed_length
    return answer
  

def compression(s, size):
    token_list = [] # [{'ab: 2}, {'cc': 1}, ...]
    pointer = 0
    while True:
      target = s[pointer:pointer+size]
      last_token = get_last_token(token_list)
      if target == last_token:
        token_list[-1][last_token] += 1 # Add the count of a meaningful token
      else:
        token_list.append({target: 1})
      pointer += size
      if pointer >= len(s):
        break
    return get_compressed_length(token_list)
    
    
def get_last_token(token_list):
    if len(token_list) == 0:
      return ''
    for key in token_list[-1].keys():
      return key
    

def get_compressed_length(token_list):
    length = 0
    for obj in token_list:
      key = [*obj][0]
      if obj[key] == 1:
        length += len(key) # ex) ab
      else:
        length += len(key) + len(str(obj[key])) # ex) 2ab
    return length