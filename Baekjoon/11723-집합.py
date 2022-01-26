import sys

def solution():
    curr = [False] * 20
  
    n = int(sys.stdin.readline().rstrip())
    
    for _ in range(n):
        oper = 0
        val = 0
        i = 0
        
        user_input = sys.stdin.readline().rstrip().split()
        if len(user_input) == 2:
            val = user_input[1]
            i = int(val) - 1    
        oper = user_input[0]
  
        if(oper == 'add'):
            curr[i] = True
        elif(oper == 'remove'):
            curr[i] = False
        elif(oper == 'check'):
            print(int(curr[i]))
        elif(oper == 'toggle'):
            curr[i] = not curr[i]
        elif(oper == 'all'):
            curr = [True] * 20
        elif(oper == 'empty'):
            curr = [False] * 20
        
solution()