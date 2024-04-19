# DPV 9.2.1

def find_vertex_cover_from_matching(G):
    vertices = set(G.keys())
    matching = []
    vertex_cover = set()   

    while vertices: 
        u = vertices.pop()
        adjacent_u = G.get(u)        
        
        for v in adjacent_u:
            if not v in vertex_cover: 
                vertices.remove(v)
                
                vertex_cover.add(u)
                vertex_cover.add(v)  
                
                matching.append((u,v))
                break
        
          


    return matching, vertex_cover

# Test

G = {1:{3},2:{4},3:{1,4,5},4:{3,2,6},5:{3},6:{4}}

matching, vertex_cover = find_vertex_cover_from_matching(G)

print(matching)

print(vertex_cover)

