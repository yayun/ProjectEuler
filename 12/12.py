import math
n=1
count=0
while count<=500:
    count=0
    N=n*(n+1)/2
    for i in range(1,int(math.sqrt(N))+1):
        if N%i==0:
            count=count+2   
        if int(math.sqrt(N))*int(math.sqrt(N))==N:
            count=count-1
    n=n+1
print N

