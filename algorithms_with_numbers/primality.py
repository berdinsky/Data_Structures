import random 

k=5 # the size of a sample 

# function for choosing a sample of size k
def sample_generator(n,k):
    numbers = list(range(2,n))
    return random.sample(numbers,k)     

# modular exponentiation a^m mod n 
def modular_exponent(a,m,n):    
    if m==0: return 1
    if m==1: return a % n
    
    if m % 2 == 0: 
        result = modular_exponent(a,m//2,n)**2 % n 
    else:  
        result = (modular_exponent(a,m//2,n)**2)*a % n
    return result 

def primality(n):
    a_list = [2,3,5,7] # or use the function sample_generator(n,k)
                       # which works badly when n is big 
    primality=True
    for a in a_list: 
        if not(modular_exponent(a,n-1,n) == 1): 
            primality=False
            break     

    return primality

# Test 

n=210662859397391326221223055831

if primality(n): 
    print(n,'is prime!')
else: 
    print(n,'is not a prime!')