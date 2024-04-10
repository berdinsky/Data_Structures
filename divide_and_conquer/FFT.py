# see DPV08, page 64 
# Input: Coefficient representation of a polynomial A(x)
# of degree <= n-1, where n is a power of 2

import cmath

pi = cmath.pi

def even_coefficients(A,n):
    A_even=[]
    for i in range(n//2):
        A_even.append(A[2*i])
    return A_even

def odd_coefficients(A,n):
    A_odd=[]
    for i in range(n//2):
        A_odd.append(A[2*i+1])
    return A_odd

def FFT(A,n):
    
    FFT_A=[]
    
    # here we check if the degree n=1
    if n==1: 
       FFT_A.append(complex(A[0],0))
       return FFT_A    
    
    A_even=even_coefficients(A,n) # get even coefficients
    A_odd=odd_coefficients(A,n) # get odd coefficients
    
    m = n // 2; A_e=FFT(A_even,m); A_o=FFT(A_odd,m)
    
    for j in range(n):  
        w_j = cmath.rect(1,2*pi*j/n)
        FFT_A.append(A_e[j % m]+w_j*A_o[j % m])    
    
    return FFT_A

# Test

n=2**3; A=[3,5,1,4,6,2,8,7] 

values = FFT(A,n)

print(values)