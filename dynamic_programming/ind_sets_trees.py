#DPV 6.7

def gr_children(Tree,children):
    grchid_list=[]
    for node in children:
        for gr_node in Tree[node]: 
            grchid_list.append(gr_node)

    return grchid_list         

def largest_set(Tree,root):
    if not Tree[root]:
        return 1
    else:
        children = Tree[root]
        grchild_list = gr_children(Tree,children)   
        m1=1 
        for node in grchild_list: m1 = m1 + largest_set(Tree,node)
        m2=0 
        for node in children: m2 = m2 + largest_set(Tree,node)

    return max(m1,m2)     

# Test

Tree = {1:[2],2:[3,4],3:[5],4:[6],5:[],6:[]}

root = 1

result  = largest_set(Tree,root)

print(result)