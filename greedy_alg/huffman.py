# DPV 5.2

import heapdict

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None

def create_node_update_heap(p_queue):
    freq1=p_queue.peekitem()[1]; node1 = p_queue.popitem()[0]     
    freq2=p_queue.peekitem()[1]; node2 = p_queue.popitem()[0] 

    node = Node() # create a new node 
    node.left = node1; node.right = node2 
    node1.parent = node; node2.parent = node

    p_queue[node]=freq1+freq2 

def build_binary_tree(p_queue,N):
    for i in range(N-2): 
        create_node_update_heap(p_queue)
    
    node1 = p_queue.popitem()[0]            
    node2 = p_queue.popitem()[0]
    node = Node() # create a root 
    node.left=node1; node.right=node2 
    node1.parent = node; node2.parent = node

    return node  # return a root

def make_nodes(input,letters): 
    p_queue = heapdict.heapdict() 
    letters_leaves={}; leaves_letters={}
    for letter in letters: 
        node= Node() # create a node
        p_queue[node]=input[letter] # add a node and a frequency to the heap
        letters_leaves[letter]=node # here for a letter we associate a node
        leaves_letters[node]=letter # here with a letter we associater a node       

    return p_queue, letters_leaves, leaves_letters      

def get_code(letter,letters_leaves):
    leaf = letters_leaves[letter]
    code = ''

    node = leaf 
    while not (node.parent==None): 
        parent =  node.parent
        if parent.left == node: code  = '0' + code 
        if parent.right == node: code = '1' + code 
        node = parent

    return code     

def print_codes(letters,letters_leaves):
    for letter in letters: 
        code = get_code(letter,letters_leaves)
        print(letter,':',code)
   
def translate(root,binary_str,leaves_letters):
    node = root 
    string=''
    length = len(binary_str)

    for i in range(length): 
        if binary_str[i]=='0': node=node.left 
        if binary_str[i]=='1': node=node.right       
        if node.left==None: 
            string = string + leaves_letters[node]
            node=root
    
    return string

# Test         
input = {'A': 0.24,'B': 0.02,'C': 0.11,'D': 0.12, 'E' : 0.16, 'F' : 0.35}
N = len(input)
letters = input.keys()

p_queue, letters_leaves ,leaves_letters = make_nodes(input, letters)


root = build_binary_tree(p_queue,N)

print_codes(letters,letters_leaves)

binary_str='001010111101010110101010'

print(translate(root,binary_str,leaves_letters))
