def solution(rows, columns, queries):
  answer = []
  mat = []
  # Generate ordered matrix
  for i in range(rows):
    mat.append([i * columns + col + 1 for col in range(columns)])

  # Rotate matrix according to queries
  for query in queries:
    mat, min_val = rotate_mat(mat, query)
    answer.append(min_val)
    
  return answer
  
  
def rotate_mat(mat, query):
  # Get query and convert to index
  (srow, scol, erow, ecol) = query
  (srow, scol, erow, ecol) = (srow-1, scol-1, erow-1, ecol-1)
  buffer = list()
  rows = [mat[srow][e] for e in range(scol, ecol+1)] + [mat[erow][e] for e in range(scol, ecol+1)]
  cols = [mat[e][scol] for e in range(srow, erow+1)] + [mat[e][ecol] for e in range(srow, erow+1)]
  min_val = min(rows + cols)
  
  # top
  buffer.append(mat[srow][ecol])
  ind = ecol
  while True:
    if(ind <= scol):
      break
    mat[srow][ind] = mat[srow][ind - 1]
    ind -= 1
  
  # right
  buffer.append(mat[erow][ecol])
  ind = erow
  while True:
    if(ind <= srow):
      break
    mat[ind][ecol] = mat[ind - 1][ecol]
    ind -= 1
  mat[srow + 1][ecol] = buffer.pop(0)
  
  # bottom
  buffer.append(mat[erow][scol])
  ind = scol
  while True:
    if(ind >= ecol):
      break
    mat[erow][ind] = mat[erow][ind + 1]
    ind += 1
  mat[erow][ecol - 1] = buffer.pop(0)
  
  # left
  ind = srow
  while True:
    if(ind >= erow):
      break
    mat[ind][scol] = mat[ind + 1][scol]
    ind += 1
  mat[erow - 1][scol] = buffer.pop(0)
  
  return (mat, min_val)