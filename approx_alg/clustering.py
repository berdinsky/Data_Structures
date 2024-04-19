# DPV 9.2.2

import math

def euclid_dist(q,r): 
    q1=q[0]; q2=q[1]; r1=r[0]; r2=r[1] 
    return math.sqrt((q1-r1)**2+(q2-r2)**2)

def min_dist(q,centers):
    dist = math.inf
    for r in centers: 
        new_dist  = euclid_dist(q,r)
        if new_dist < dist: 
            dist = new_dist
   
    return dist  

def k_clustering(P,k):
    
    s = P.pop() 
    centers = {s}

    for i in range(1,k):
        
        current_dist = 0
        for q in P:
            new_min_dist = min_dist(q,centers)
            if new_min_dist > current_dist: 
                current_dist = new_min_dist 
                center_point = q
        
        centers.add(center_point)
        P.remove(center_point)

    return centers

def cluster(center_point,centers,P): 
    cluster_points = {center_point}
    for q in P: 
        if euclid_dist(q,center_point) == min_dist(q,centers):
            cluster_points.add(q)
    
    return cluster_points

# Test 

P = {(2.4,3.1),(1.1,2.3),(1.3,4.5),(1.4,3.3),(1.7,4.2),(3.2,2.9)} 
k=3

centers = k_clustering(P,k) 

for center_point in centers: 
    cluster_points = cluster(center_point,centers,P)
    print(cluster_points)



































