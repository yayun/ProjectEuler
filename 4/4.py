import math
s=[0,0,0,0,0,0,0]
m=0
n=0
max=1
for i in range(999,101,-1):
    for j in range(999,101,-1):
        Mu=i*j
        k=10
        while Mu>=1:
            s[m]=Mu%10
            Mu=Mu/10
            m=m+1
        k=m-1
        m=0
        n=0
        Mu=i*j
        while s[n]==s[k] and k>=n:
           k=k-1
           n=n+1
           if k==n or k<n:
               if Mu>max:
                   max=Mu
print max

