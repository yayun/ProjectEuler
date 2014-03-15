def test(i):
    k=0
    while i>1:
        if i%2==0:
            i=i/2
        else:
            i=3*i+1
        k=k+1
    return k
def main():
    max=0
    maxi=0
    for i in range(1,1000000):
        if (2*i)%2==((i-1)/3)%2==0:
            num=test(i)
            print i,num
            if num>max:
                max=num
                maxi=i
    print maxi
main()           
                
