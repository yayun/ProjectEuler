def fun(a,b):
    while a%b!=0:
        k=a%b
        a=b
        b=k
    return b
i=1
for j in range(2,21):
    i=i*j/fun(i,j)
print i

        


