D=[[0,31,29,31,30,31,30,31,31,30,31,30,31],[0,31,28,31,30,31,30,31,31,30,31,30,31]]
day=0
sum=0
for Y in range(1900,2001):
    if Y%4==0 and Y%100!=0 and Y%400==0:
        for M in range(1,13):
            if (day+1)%7==0 and Y>1900:
                sum=sum+1
            day=day+D[0][M]
            
    else:
        for M in range(1,13):
            if (day+1)%7==0 and Y>1900:
                sum=sum+1
            day=day+D[1][M]             
            
print sum

