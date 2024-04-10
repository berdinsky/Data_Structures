# DPV 5.4

def find_cover(S,U): 
    cover=[]
    while U:
        max = 0 
        for s in S: 
            if len(U.intersection(s))>max: 
                best_s = s 
                max = len(U.intersection(s))
       
        cover.append(best_s)    
        S.remove(s)
        U=U.difference(best_s)
        
    return cover

# Test 

B = {1,2,3,4,5,6}

S =[{1,4,6},{1,2,4},{2,3,5},{3,6},{2,5},{3,4,5}]

cover = find_cover(S,B)

print(cover)