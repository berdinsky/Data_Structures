# DPV 6.3

def edit_distance(word1,word2): 
    m = len(word1); n = len(word2)
            
    E = [[0 for x in range(n+1)] for y in range(m+1)]
    
    for i in range(m+1): E[i][0]=i
    for j in range(1,n+1): E[0][j]=j
     
    for i in range(1,m+1): 
        for j in range(1,n+1): 
            
            if word1[i-1]==word2[j-1]: diff = 0 # computing diff 
            else:  diff = 1
            
            E[i][j]=min(E[i-1][j]+1,E[i][j-1]+1,E[i-1][j-1]+diff) 
        
    return E[m][n]

# Test

word1 = 'EXPONENTIAL'
word2 = 'POLYNOMIAL'

distance = edit_distance(word1,word2)

print(distance)