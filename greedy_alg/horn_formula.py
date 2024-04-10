# DPV 5.3

def eval(left_side,assignment):
    bool = True
    for i in left_side:
        if not assignment[i]: # if the value is False
            bool = False
            break
    
    return bool    

def check_implications(implications,assignment):
    change=True
    while change:
        change=False
        for implication in implications: 
            right_side = implication[1]
            if not assignment[right_side]: # if the right side is False
                left_side=implication[0]
                if eval(left_side,assignment):
                    assignment[right_side] = True    
                    change=True
    
    return assignment

def check_negative_clauses(neg_clauses,assignment):
    for clause in neg_clauses:
      satisfied = False
      for i in clause:
        if not assignment[i]: 
            satisfied = True     
      if not satisfied: return False 
          
    return True             

def initial_set(N,singleton_implications):
    assignment=[]
    for i in range(N): 
        assignment.append(False)
    for j in singleton_implications:
        assignment[j]=True 

    return assignment

# Test 
N=4 
implications = [[[1,2],0],[[0],1]]
singleton_implications=[1]
neg_clauses = [[3,0,1],[2]]

assignment = initial_set(N,singleton_implications)

check_implications(implications,assignment)

if check_negative_clauses(neg_clauses,assignment):
    print('satisfied: ',assignment) 
else: 
    print('not satisfied')
