'''
let k=2,3,4,5... if k is a factor of N,it will necessory be a prime
'''
N=600851475143 
i=2
max=1
while i<=N:
    if N==i:
        print N
    if N%i==0:
        N=N/i
    if N%i!=0:#have same factor
        i=i+1
