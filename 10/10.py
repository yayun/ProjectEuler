import math
sum=0
for i in range(2,2000000):
    for j in range(2,i):
        if i%j==0:
            break
        if j==i-1:
            print i
            sum=sum+i
print sum
