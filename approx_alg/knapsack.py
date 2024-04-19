# rescaling of values is skipped in this implementation

import math

def K(weights,values,n,V):

    K = [[math.inf for j in range(n+1)] for i in range(V+1)] 
  
    for j in range(1,n+1):    
        for i in range(1,V+1):
            v_j = values[j-1]; w_j = weights[j-1]           
            if v_j > i: 
                K[i][j]=K[i][j-1]
            elif v_j == i:
                K[i][j]=min(K[i][j-1],w_j)
            else:# if v_j < i 
                K[i][j]=min(K[i][j-1],K[i-v_j][j-1]+w_j)
    
    return K  

def print_K(K,n,V):
    for i in range(1,V+1):
        print(K[i][n], end = ' ')
    print('\n')

def sum_values(n,values): 
    V = 0 
    for i in range(n): V=V+values[i]
    
    return V

# Test 

weights = [3,1,5,2,6,4]; values = [10,3,20,5,30,11]

n = len(values); V = sum_values(n,values)

K = K(weights,values,n,V)

print_K(K,n,V)














































