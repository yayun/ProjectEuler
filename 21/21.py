import math
k=0
m=0
sum=0
for i in range(1,10001):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            if math.pow(j,2)==i:
                k=k+j
            else:
                k=k+j+i/j
    if k>0:
        k=k+1
        for n in range(2,int(math.sqrt(k))+1):
            if k%n==0:
                if math.pow(n,2)==k:
                    m=m+n
                else:
                    m=m+n+k/n
        m=m+1
    if m==i and k!=m:
        print i,k
        sum=sum+m
    k=m=0
print sum


