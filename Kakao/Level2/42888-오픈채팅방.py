def solution(record):
  stack = []
  relation = {}
  
  for stm in record:
    split_stm = stm.split(' ')
    if len(split_stm) == 2: # Leave
      leave(split_stm[1], stack)
    else: # Enter or Change
      (action, uuid, name) = split_stm
      if action == 'Enter':
        enter(uuid, name, stack, relation)
      if action == 'Change':
        change(uuid, name, relation)
  
  answer = create_answer(stack, relation)
  return answer
  
  
def enter(uuid, name, stack, relation):
  relation[uuid] = name
  stack.append(('Enter', uuid))

def leave(uuid, stack):
  stack.append(('Leave', uuid))

def change(uuid, new_name, relation):
  relation[uuid] = new_name
  
def create_answer(stack, relation):
  answer = []
  for stm in stack:
    (action, uuid) = stm
    name = relation[uuid]
    ans_stm = name+'님이 '
    if action == 'Enter':
      ans_stm += '들어왔습니다.'
    if action == 'Leave':
      ans_stm += '나갔습니다.'
    answer.append(ans_stm)
  return answer
