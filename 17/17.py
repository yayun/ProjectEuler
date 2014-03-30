m=k=0
def words(m):
    if m in [1,2,6]:
        return 3
    elif m in [3,7,8]:
        return 5
    elif m in [4,5,9]:
        return 4
    else :
        return 0
def word(m):
    if m in [2,3,8,9]:
        return 6
    elif m==7:
        return 7
    elif m in [4,5,6]:
        return 5
    else :
        return 0
def ten_words(k):
    if k<10:
        return words(k)
    if 9<k<20:
        if k==10:
            return 3
        elif k in [11,12]:
            return 6
        elif k in [13,14,18,19]:
            return 8
        elif k in [15,16]:
            return 7
        if k==17:
            return 9
    if 19<k<100:
        x=k/10
        y=k%10
        return word(x)+words(y)
    else :
        return 0
def cal(n):
    if n<10:
        return words(n)
    if 9<n<100:
        return ten_words(n)
    if n>99:
        i=n/100
        j=n%100
        if j==0:
            return words(i)+7
        else:
            return words(i)+10+ten_words(j)

sum=0
for i in range(1,1000):
    sum=sum+cal(i)
print sum+len("onethousand")
